# Pizza Demand Forecasting

## Overview
This repository contains the code and dataset used for forecasting pizza demand using SARIMA (Seasonal AutoRegressive Integrated Moving Average) time series modeling.

## Project Structure

- `Order_System_2.csv`: The dataset containing historical pizza order information.
- `Pizza_prediction.ipynb`: Jupyter notebook with the SARIMA model development and validation.
- `pizza_order.gs`: Google Script file associated with the project and the monitoring system.

## Model
The SARIMA model is used to predict daily pizza demand, considering seasonality, holidays, and other relevant factors. The model helps to estimate the required inventory to meet the upcoming demand.

## Usage
To replicate the forecasting process or to run the predictive model on new data:
1. Ensure you have Python installed with the required libraries (`pandas`, `matplotlib`, `statsmodels`).
2. Load the `Pizza_prediction.ipynb` notebook in a Jupyter environment.
3. Run the cells sequentially to perform the time series analysis and to generate forecasts.

## Results
The model's performance is evaluated using the Root Mean Squared Error (RMSE) metric, indicating the average deviation of the predicted values from the actual values. The lower the RMSE, the better the model's forecasts.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
If you have any questions or comments about this project, please open an issue in this repository.
