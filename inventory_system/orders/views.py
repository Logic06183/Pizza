# orders/views.py

from django.shortcuts import render, redirect
from .models import PizzaOrder
from .forms import PizzaOrderForm
from datetime import datetime, timedelta
import pytz
from inventory.models import Ingredient

def add_order(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.pizza_type = form.cleaned_data['pizza_type']
            pizza_order.quantities = form.cleaned_data['quantities']
            pizza_order.save()
            return redirect('order_list')
    else:
        form = PizzaOrderForm()
    return render(request, 'orders/add_order.html', {'form': form})

def order_list(request):
    orders = PizzaOrder.objects.filter(display=True)
    current_time = datetime.now(pytz.timezone('Africa/Johannesburg'))  # Use timezone-aware datetime
    order_list = []
    for order in orders:
        due_time = order.order_time + timedelta(minutes=order.preparation_time)
        order.is_late = current_time > due_time
        order.is_high_priority = current_time + timedelta(minutes=5) > due_time and not order.is_late
        order_list.append((order, due_time))
    order_list.sort(key=lambda x: x[1])  # Sort by due_time
    return render(request, 'orders/order_list.html', {'orders': order_list})

def daily_report(request):
    # Calculate the estimated usage of ingredients for the current day
    orders = PizzaOrder.objects.filter(order_time__date=datetime.today().date())
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
