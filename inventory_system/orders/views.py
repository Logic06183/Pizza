from django.shortcuts import render, redirect
from .models import PizzaOrder, Pizza, PizzaOrderItem
from .forms import PizzaOrderForm
from inventory.models import Ingredient  # This import should now work correctly
  # Ensure Ingredient is imported from the correct app


def add_order(request):
    pizzas = Pizza.objects.all()  # Ensure all pizzas are fetched
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.save()

            # Save the pizza quantities
            for pizza in pizzas:
                quantity = int(request.POST.get(f'quantity_{pizza.id}', 0))
                if quantity > 0:
                    PizzaOrderItem.objects.create(order=pizza_order, pizza_type=pizza, quantity=quantity)

            return redirect('order_list')
    else:
        form = PizzaOrderForm()

    return render(request, 'orders/add_order.html', {'form': form, 'pizzas': pizzas})


def order_list(request):
    orders = PizzaOrder.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

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

from django.utils import timezone
from datetime import timedelta

def order_list(request):
    today = timezone.now().date()
    orders = PizzaOrder.objects.filter(order_time__date=today, display=True)
    current_time = timezone.now()

    order_list = []
    for order in orders:
        due_time = order.order_time + timedelta(minutes=order.preparation_time)
        order.is_late = current_time > due_time
        order.is_high_priority = current_time + timedelta(minutes=5) > due_time and not order.is_late
        pizza_types = [item.pizza_type.name for item in order.pizzaorderitem_set.all()]
        quantities = [item.quantity for item in order.pizzaorderitem_set.all()]
        order_list.append((order, due_time, pizza_types, quantities))  # List of tuples with 4 elements

    order_list.sort(key=lambda x: x[1])  # Sort by due_time
    return render(request, 'orders/order_list.html', {'orders': order_list})
