from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import WeeklyStock, DailyStock, Ingredient
from .forms import WeeklyStockForm, DailyStockForm
from orders.models import PizzaOrder
from datetime import datetime, timedelta
import pytz

def weekly_stock_list(request):
    try:
        date_today = datetime.today().date()
        start_of_week = date_today - timedelta(days=date_today.weekday())
        
        # Get weekly stock
        stock = WeeklyStock.objects.filter(date__gte=start_of_week).latest('date')
        
        # Calculate ingredient usage from orders
        orders = PizzaOrder.objects.filter(order_time__date__gte=start_of_week)
        ingredient_usage = {}
        for order in orders:
            usage = order.calculate_ingredient_usage()
            for ingredient, amount in usage.items():
                if ingredient not in ingredient_usage:
                    ingredient_usage[ingredient] = 0
                ingredient_usage[ingredient] += amount
        
        # Prepare report data
        report = []
        for item in stock._meta.fields:
            if item.name.endswith("_new_delivery"):
                ingredient = item.name.replace("_new_delivery", "")
                initial_stock = getattr(stock, f"{ingredient}_closing_stock")
                new_delivery = getattr(stock, item.name)
                closing_stock = initial_stock - ingredient_usage.get(ingredient, 0) + new_delivery
                usage = ingredient_usage.get(ingredient, 0)
                
                report.append({
                    'name': ingredient.replace('_', ' ').title(),
                    'initial_stock': initial_stock,
                    'new_delivery': new_delivery,
                    'closing_stock': closing_stock,
                    'usage': usage
                })
    except ObjectDoesNotExist:
        report = None

    return render(request, 'inventory/weekly_stock_list.html', {'report': report})

def add_weekly_stock(request):
    if request.method == 'POST':
        form = WeeklyStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weekly_stock_list')
    else:
        form = WeeklyStockForm()
    return render(request, 'inventory/add_weekly_stock.html', {'form': form})

def daily_stock_list(request):
    try:
        date_today = datetime.today().date()
        
        # Get daily stock
        stock = DailyStock.objects.filter(date=date_today).latest('date')
        
        # Calculate ingredient usage from orders
        orders = PizzaOrder.objects.filter(order_time__date=date_today)
        ingredient_usage = {}
        for order in orders:
            usage = order.calculate_ingredient_usage()
            for ingredient, amount in usage.items():
                if ingredient not in ingredient_usage:
                    ingredient_usage[ingredient] = 0
                ingredient_usage[ingredient] += amount
        
        # Prepare report data
        report = []
        for item in stock._meta.fields:
            if item.name.endswith("_new_delivery"):
                ingredient = item.name.replace("_new_delivery", "")
                initial_stock = getattr(stock, f"{ingredient}_closing_stock")
                new_delivery = getattr(stock, item.name)
                closing_stock = initial_stock - ingredient_usage.get(ingredient, 0) + new_delivery
                usage = ingredient_usage.get(ingredient, 0)
                
                report.append({
                    'name': ingredient.replace('_', ' ').title(),
                    'initial_stock': initial_stock,
                    'new_delivery': new_delivery,
                    'closing_stock': closing_stock,
                    'usage': usage
                })
    except ObjectDoesNotExist:
        report = None

    return render(request, 'inventory/daily_stock_list.html', {'report': report})

def add_daily_stock(request):
    if request.method == 'POST':
        form = DailyStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_stock_list')
    else:
        form = DailyStockForm()
    return render(request, 'inventory/add_daily_stock.html', {'form': form})

from django.shortcuts import render
from .models import WeeklyStock
from datetime import datetime, timedelta
import pytz
from django.db import models

def weekly_stock_report(request):
    today = datetime.now(pytz.timezone('Africa/Johannesburg')).date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    weekly_stocks = WeeklyStock.objects.filter(date__range=[start_of_week, end_of_week])
    total_usage = {}

    for stock in weekly_stocks:
        for field in stock._meta.get_fields():
            if hasattr(field, 'name') and isinstance(field, models.IntegerField) and field.name.endswith('_new_delivery'):
                ingredient_name = field.name.replace('_new_delivery', '')
                usage_field = f"{ingredient_name}_closing_stock"
                if ingredient_name not in total_usage:
                    total_usage[ingredient_name] = {'new_delivery': 0, 'closing_stock': 0}
                total_usage[ingredient_name]['new_delivery'] += getattr(stock, field.name)
                total_usage[ingredient_name]['closing_stock'] += getattr(stock, usage_field)

    report = []
    for ingredient, data in total_usage.items():
        initial_stock = data['new_delivery'] - data['closing_stock']
        usage = initial_stock - data['closing_stock']
        report.append({
            'name': ingredient.replace('_', ' ').title(),
            'initial_stock': initial_stock,
            'new_delivery': data['new_delivery'],
            'closing_stock': data['closing_stock'],
            'usage': usage
        })

    return render(request, 'inventory/weekly_stock_report.html', {'report': report})


