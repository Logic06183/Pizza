function movePastOrders() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('Form Responses 1');
  var pastOrdersSheet = spreadsheet.getSheetByName("Past Orders");

  if (!pastOrdersSheet) {
    pastOrdersSheet = spreadsheet.insertSheet("Past Orders");
  }

  var rows = sheet.getDataRange().getValues();
  var today = new Date();
  today.setHours(0, 0, 0, 0);

  // Starting from the last row to avoid index issues when deleting rows
  for (var r = rows.length - 1; r >= 1; r--) {
    var timestamp = new Date(rows[r][0]);
    if (timestamp < today) {
      // This is a past order, so move it to the past orders sheet
      var rowRange = sheet.getRange(r + 1, 1, 1, sheet.getLastColumn());
      var rowData = rowRange.getValues()[0];

      // Combine the pizzas into a single list
      var combinedPizzas = [];
      for (var i = 2; i <= 4; i++) { // Assuming Pizzas [1] is in column C, Pizzas [2] in D, and Pizzas [3] in E
        if (rowData[i]) {
          combinedPizzas = combinedPizzas.concat(rowData[i].toString().split(',').map(function(pizza) { return pizza.trim(); }));
        }
      }

      // Insert a new row at the bottom of the past orders sheet
      var lastRow = pastOrdersSheet.getLastRow() + 1;
      pastOrdersSheet.insertRowAfter(lastRow);

      // Copy the original row data except the pizza columns
      for (var col = 1; col <= rowData.length; col++) {
        if (col < 3 || col > 5) { // Skip pizza columns
          pastOrdersSheet.getRange(lastRow, col).setValue(rowData[col - 1]);
        }
      }

      // Set the combined pizzas into their own columns, starting after the original data columns
      combinedPizzas.forEach(function(pizza, index) {
        pastOrdersSheet.getRange(lastRow, sheet.getLastColumn() + index).setValue(pizza);
      });

      // Delete the original row from the 'Form Responses 1' sheet
      sheet.deleteRow(r + 1);
    }
  }
}





function sortOrders() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Form Responses 1'); // Specify the sheet name explicitly
  var lastRow = sheet.getLastRow();
  var range = sheet.getRange("A2:H" + lastRow); // Adjust the range to include columns A to H

  // Sorting by the 8th column (Column H), which contains the "Order is Due" time
  range.sort({column: 8, ascending: true});
}


function onFormSubmit(e) {
  var sheet = e.range.getSheet();
  var row = e.range.getRow();

  // Ensure we are on the correct sheet
  if(sheet.getName() == 'Form Responses 1') {
    var prepTimeCell = sheet.getRange(row, 7); // Preparation Time is in column G (7th column)
    var timestampCell = sheet.getRange(row, 1); // Timestamp is in column A (1st column)
    var orderIsDueCell = sheet.getRange(row, 8); // "Order is Due" is in column H (8th column)

    var prepTimeValue = prepTimeCell.getValue();
    var timestampValue = timestampCell.getValue();

    // Check if prep time is a number and timestamp is a date
    if (!isNaN(prepTimeValue) && timestampValue instanceof Date) {
      var prepTimeMinutes = parseInt(prepTimeValue);
      var timestamp = new Date(timestampValue);

      // Calculate the order due time by adding the prep time to the order time
      var orderDueTime = new Date(timestamp.getTime() + prepTimeMinutes * 60000);

      // Write the order due time back to the "Order is Due" cell in HH:mm format
      var hours = orderDueTime.getHours();
      var minutes = orderDueTime.getMinutes();

      // Pad the minutes with leading zeros if needed
      var formattedTime = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes);

      orderIsDueCell.setValue(formattedTime);
    } else {
      // If data is not valid, log an error or set a default value
      orderIsDueCell.setValue('Invalid Data');
      Logger.log('Invalid timestamp or preparation time. Row: ' + row);
    }
  }
}

function updateOrderStatuses() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Form Responses 1');
  var lastRow = sheet.getLastRow();
  var ordersRange = sheet.getRange("A2:I" + lastRow);
  var ordersData = ordersRange.getValues();

  var currentTime = new Date();

  // Loop through all orders and update the "Status" column
  for (var i = 0; i < ordersData.length; i++) {
    var orderDueTime = new Date(ordersData[i][7]);
    var statusCell = sheet.getRange(i + 2, 9); // "Status" is in column I (9th column)

    if (currentTime > orderDueTime) {
      statusCell.setValue('Late');
      statusCell.setFontColor('red');
    } else {
      statusCell.setValue('On Time');
      statusCell.setFontColor('black');
    }
  }
}


function onEdit(e) {
  var range = e.range;
  var sheet = range.getSheet();

  // Check if the edit was made on the correct sheet and in the correct column (J)
  if (sheet.getName() === 'Form Responses 1' && range.getColumn() === 10) {
    var row = range.getRow();
    var checkboxChecked = range.isChecked();
    var statusCell = sheet.getRange(row, 9); // "Status" is in column I (9th column)

    // If the checkbox is checked, set the "Status" font color to green, otherwise to black
    if (checkboxChecked) {
      statusCell.setFontColor('green');
    } else {
      // Optionally, you can change the font color to something else when unchecked
      statusCell.setFontColor('black');
    }
  }
}


function processPizzaOrders() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var pastOrdersSheet = ss.getSheetByName('Past Orders');
  var lookupSheet = ss.getSheetByName('Lookup');
  var resultSheetName = 'Daily Ingredient Usage';
  var resultSheet = ss.getSheetByName(resultSheetName) || ss.insertSheet(resultSheetName);

  var pastOrdersData = pastOrdersSheet.getDataRange().getValues();
  var lookupData = lookupSheet.getDataRange().getValues();
  var totalIngredients = {};

  // Helper function to normalize pizza names for comparison
  function normalizePizzaName(name) {
    return (name + '').trim().toLowerCase().replace(/'s| in | the | pizza/g, "");
  }

  // Create a map for efficient lookup of ingredients by pizza name
  var lookupMap = {};
  lookupData.slice(1).forEach(function(row) { // Skip header row
    var pizzaName = normalizePizzaName(row[0]);
    if (!lookupMap[pizzaName]) {
      lookupMap[pizzaName] = [];
    }
    lookupMap[pizzaName].push({ ingredient: row[1], quantity: parseFloat(row[2]), cost: parseFloat(row[3]) });
  });

  // Determine yesterday's date
  var today = new Date();
  var yesterday = new Date(today);
  yesterday.setDate(today.getDate() - 1);
  yesterday.setHours(0, 0, 0, 0); // Normalize yesterday's date to start of the day for comparison

  // Filter past orders to include only those from yesterday
  var filteredOrdersData = pastOrdersData.slice(1).filter(function(order) { // Skip header row
    var orderDate = new Date(order[0]);
    return orderDate >= yesterday && orderDate < today;
  });

  // Loop through filtered past orders and aggregate ingredients
  filteredOrdersData.forEach(function(order) {
    // Starting from the 10th column (J) where the pizzas are listed
    for (var i = 9; i < order.length; i++) {
      var pizzaCellContent = order[i];
      if (pizzaCellContent && typeof pizzaCellContent === 'string') {
        var pizzaName = normalizePizzaName(pizzaCellContent);
        if (lookupMap[pizzaName]) {
          lookupMap[pizzaName].forEach(function(lookupRow) {
            var ingredient = lookupRow.ingredient;
            var quantity = lookupRow.quantity;
            if (!totalIngredients[ingredient]) {
              totalIngredients[ingredient] = { totalQuantity: 0, totalCost: 0 };
            }
            totalIngredients[ingredient].totalQuantity += quantity;
            // Assuming cost calculation is not needed for daily usage, remove or comment out the totalCost line if unnecessary
            totalIngredients[ingredient].totalCost += lookupRow.cost;
          });
        }
      }
    }
  });

  // Prepare the data to be written to the 'Daily Ingredient Usage' sheet
  var resultData = [["Ingredient", "Total Quantity", "Total Cost"]];
  Object.keys(totalIngredients).forEach(function(ingredient) {
    resultData.push([
      ingredient,
      totalIngredients[ingredient].totalQuantity,
      totalIngredients[ingredient].totalCost.toFixed(2) // Round to 2 decimal places for cost
    ]);
  });

  // Write the data to the result sheet
  resultSheet.clear();
  resultSheet.getRange(1, 1, resultData.length, 3).setValues(resultData);
}







function summarizeOrders() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ordersSheet = ss.getSheetByName('Past Orders');
  var summarySheet = ss.getSheetByName('Inventory Summary') || ss.insertSheet('Inventory Summary');

  // Clear the previous summary
  summarySheet.clear();

  // Retrieve all orders
  var ordersData = ordersSheet.getDataRange().getValues();
  var pizzaSummary = {};

  ordersData.slice(1).forEach(function(row) { // Skip header row
    // Starting from the 10th column (J) where the pizzas are listed
    for (var i = 9; i < row.length; i++) {
      var cellContent = row[i];
      // Check if the cell content is a non-empty string before processing
      if (cellContent && typeof cellContent === 'string') {
        var pizzaName = cellContent.trim().toLowerCase();
        pizzaSummary[pizzaName] = (pizzaSummary[pizzaName] || 0) + 1;
      }
    }
  });

  // Convert the summary object to an array suitable for the spreadsheet
  var summaryArray = [["Pizza Name", "Total Count"]];
  Object.keys(pizzaSummary).forEach(function(name) {
    summaryArray.push([name, pizzaSummary[name]]);
  });

  // Write the summary to the sheet
  summarySheet.getRange(1, 1, summaryArray.length, 2).setValues(summaryArray);
}


function summarizeOrdersWithDateFilter() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var dashboardSheet = ss.getSheetByName('Dashboard');
  var startDate = new Date(dashboardSheet.getRange('A1').getValue());
  var endDate = new Date(dashboardSheet.getRange('A2').getValue());
  var ordersSheet = ss.getSheetByName('Past Orders');
  var summarySheet = ss.getSheetByName('Inventory Summary') || ss.insertSheet('Inventory Summary');

  // Clear the previous summary
  summarySheet.clear();

  // Retrieve all orders
  var ordersData = ordersSheet.getDataRange().getValues();
  var pizzaSummary = {};

  ordersData.slice(1).forEach(function(row) { // Skip header row
    var orderDate = new Date(row[0]);
    if (orderDate >= startDate && orderDate <= endDate) {
      // Starting from the 10th column (J) where the pizzas are listed
      for (var i = 9; i < row.length; i++) {
        var cellContent = row[i];
        // Check if the cell content is a non-empty string before processing
        if (cellContent && typeof cellContent === 'string') {
          var pizzaName = cellContent.trim().toLowerCase();
          pizzaSummary[pizzaName] = (pizzaSummary[pizzaName] || 0) + 1;
        }
      }
    }
  });

  // Convert the summary object to an array suitable for the spreadsheet
  var summaryArray = [["Pizza Name", "Total Count"]];
  Object.keys(pizzaSummary).forEach(function(name) {
    summaryArray.push([name, pizzaSummary[name]]);
  });

  // Write the summary to the sheet
  summarySheet.getRange(1, 1, summaryArray.length, 2).setValues(summaryArray);
}









