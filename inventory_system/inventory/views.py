from django.shortcuts import render, redirect
from django.db import transaction
from .models import WeeklyStock, DailyStock, StockItem, StockRecord
from .forms import WeeklyStockForm, DailyStockForm, StockRecordForm

# Reusable function to handle stock form submissions
def handle_stock_form(request, stock_form_class, template_name, redirect_name):
    stock_items = StockItem.objects.all()
    if request.method == 'POST':
        stock_form = stock_form_class(request.POST)
        if stock_form.is_valid():
            with transaction.atomic():
                stock_instance = stock_form.save()

                stock_records = []
                for item in stock_items:
                    new_delivery = request.POST.get(f'new_delivery_{item.id}', 0)
                    closing_stock = request.POST.get(f'closing_stock_{item.id}', 0)
                    order_required = request.POST.get(f'order_required_{item.id}', 'off') == 'on'

                    if int(new_delivery) > 0 or int(closing_stock) > 0:
                        stock_record = StockRecord(
                            stock=stock_instance,
                            item=item,
                            new_delivery=int(new_delivery),
                            closing_stock=int(closing_stock),
                            order_required=order_required
                        )
                        stock_records.append(stock_record)

                StockRecord.objects.bulk_create(stock_records)
            return redirect(redirect_name)
    else:
        stock_form = stock_form_class()

    return render(request, template_name, {
        'form': stock_form,
        'stock_items': stock_items,
    })

# View to add weekly stock
def add_weekly_stock(request):
    return handle_stock_form(request, WeeklyStockForm, 'inventory/add_weekly_stock.html', 'weekly_stock_list')

# View to add daily stock
def add_daily_stock(request):
    return handle_stock_form(request, DailyStockForm, 'inventory/add_daily_stock.html', 'daily_stock_list')

# View to list all stocks
def stock_list(request):
    stocks = StockItem.objects.all()
    return render(request, 'inventory/stock_list.html', {'stocks': stocks})

from django.shortcuts import render, redirect
from django.db import transaction
from .models import DailyStock, StockItem, StockRecord
from .forms import DailyStockForm

def daily_stock_list(request):
    if request.method == 'POST':
        with transaction.atomic():
            # Process each stock item update
            for stock in StockItem.objects.all():
                new_quantity = request.POST.get(f'quantity_{stock.id}', None)
                if new_quantity is not None:
                    stock.quantity = int(new_quantity)
                    stock.save()

            # Optional: Handle adding new stock items if that functionality is required
            new_stock_name = request.POST.get('new_stock_name', None)
            new_stock_quantity = request.POST.get('new_stock_quantity', None)
            if new_stock_name and new_stock_quantity:
                StockItem.objects.create(name=new_stock_name, quantity=int(new_stock_quantity))

        return redirect('daily_stock_list')  # Redirect to the same view to show updated data

    stocks = StockItem.objects.all()
    return render(request, 'inventory/daily_stock_list.html', {'stocks': stocks})


# View to list all weekly stocks
def weekly_stock_list(request):
    stocks = WeeklyStock.objects.all()
    return render(request, 'inventory/weekly_stock_list.html', {'stocks': stocks})

# View to generate weekly stock report
def weekly_stock_report(request):
    stocks = WeeklyStock.objects.all()
    return render(request, 'inventory/weekly_stock_report.html', {'stocks': stocks})

from django.shortcuts import render
from .models import PizzaOrder, Ingredient  # Ensure Ingredient is imported
from django.utils import timezone

def daily_report(request):
    # Calculate the estimated usage of ingredients for the current day
    orders = PizzaOrder.objects.filter(order_time__date=timezone.now().date())
    total_usage = {}
    for order in orders:
        usage = order.calculate_ingredient_usage()
        for ingredient, quantity in usage.items():
            if ingredient not in total_usage:
                total_usage[ingredient] = 0
            total_usage[ingredient] += quantity

    # Calculate remaining stock based on current inventory
    ingredients = Ingredient.objects.all()
    report = []
    for ingredient in ingredients:
        remaining_quantity = ingredient.quantity - total_usage.get(ingredient.name, 0)
        report.append({
            'name': ingredient.name,
            'current_stock': ingredient.quantity,
            'estimated_usage': total_usage.get(ingredient.name, 0),
            'estimated_remaining': remaining_quantity,
        })

    return render(request, 'orders/daily_report.html', {'report': report})
