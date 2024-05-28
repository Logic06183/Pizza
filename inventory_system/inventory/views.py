from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import WeeklyStock, Ingredient
from .forms import WeeklyStockForm, IngredientForm
from django.shortcuts import render, redirect
from .models import DailyStock
from .forms import DailyStockForm

def weekly_stock_list(request):
    try:
        stock = WeeklyStock.objects.latest('date')
        items = [
            ('Pizza Box', 'pizza_box'),
            ('Cooking Oil', 'cooking_oil'),
            ('Salt', 'salt'),
            ('Sugar', 'sugar'),
            ('Dishwashing Liquid', 'dishwashing_liquid'),
            ('Bleach', 'bleach'),
            ('Pine Gel', 'pine_gel'),
            ('Black Bags', 'black_bags'),
            ('Hand-soap', 'hand_soap'),
            ('Apron Washing Powder', 'apron_washing_powder'),
            ('Coke 0', 'coke_zero'),
            ('Coke', 'coke'),
            ('Fanta', 'fanta'),
            ('Iced Tea Peach', 'iced_tea_peach'),
            ('Iced Tea Lemon', 'iced_tea_lemon'),
            ('Still Water', 'still_water'),
            ('Sparkling Water', 'sparkling_water'),
            ('Sprite', 'sprite'),
            ('Heineken 0%', 'heineken_zero'),
            ('Savanna 0%', 'savanna_zero'),
            ('Flour (White)', 'flour_white'),
            ('Paper Towel (Roller)', 'paper_towel'),
            ('Serviette', 'serviette'),
            ('Straws', 'straws'),
            ('Foil', 'foil'),
            ('Clingwrap', 'clingwrap'),
            ('Chilli', 'chilli'),
            ('Garlic', 'garlic'),
        ]
        stock_items = {
            'date': stock.date,
            'staff_name': stock.staff_name,
            'items': [
                {
                    'name': item[0],
                    'new_delivery': getattr(stock, f"{item[1]}_new_delivery"),
                    'closing_stock': getattr(stock, f"{item[1]}_closing_stock"),
                    'order_required': getattr(stock, f"{item[1]}_order_required"),
                }
                for item in items
            ]
        }
    except ObjectDoesNotExist:
        stock_items = None

    return render(request, 'inventory/weekly_stock_list.html', {'stock': stock_items})

def add_weekly_stock(request):
    if request.method == 'POST':
        form = WeeklyStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weekly_stock_list')
    else:
        form = WeeklyStockForm()
    return render(request, 'inventory/add_weekly_stock.html', {'form': form})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'inventory/add_ingredient.html', {'form': form})

def add_daily_stock(request):
    if request.method == 'POST':
        form = DailyStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_stock_list')
    else:
        form = DailyStockForm()
    return render(request, 'inventory/add_daily_stock.html', {'form': form})

def daily_stock_list(request):
    daily_stocks = DailyStock.objects.all().order_by('-date')
    return render(request, 'inventory/daily_stock_list.html', {'daily_stocks': daily_stocks})


from django.shortcuts import render
from .models import WeeklyStock, Ingredient
from datetime import datetime, timedelta
import pytz

def weekly_stock_report(request):
    today = datetime.now(pytz.timezone('Africa/Johannesburg')).date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    weekly_stocks = WeeklyStock.objects.filter(date__range=[start_of_week, end_of_week])
    total_usage = {}

    for stock in weekly_stocks:
        for field in stock._meta.get_fields():
            if isinstance(field, models.IntegerField) and field.name.endswith('_new_delivery'):
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

