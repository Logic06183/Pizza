from django.shortcuts import render, redirect
from .models import Order, Pizza, OrderItem, Topping  # Updated imports
from .forms import OrderForm  # Remove PizzaOrderForm
from inventory.models import Ingredient  # This import should now work correctly
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django import forms

class OrderForm(forms.Form):
    PLATFORM_CHOICES = [
        ('web', 'Website'),
        ('app', 'Mobile App'),
    ]
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)
    customer = forms.CharField(max_length=100, required=False)

def add_order(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'toppings': Topping.objects.all()
    }
    return render(request, 'orders/add_order.html', context)

def order_list(request):
    active_orders = Order.objects.prefetch_related('orderitem_set__pizza').filter(
        status__in=['pending', 'preparing', 'ready']
    ).order_by('due_time')
    
    context = {
        'active_orders': active_orders,
    }
    return render(request, 'orders/order_list.html', context)

@csrf_exempt
def update_order_status(request, order_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')
        
        try:
            order = Order.objects.get(id=order_id)
            order.status = status
            if status == 'completed':
                order.completed_time = timezone.now()
            order.save()
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Order not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_orders(request):
    active_orders = Order.objects.filter(
        status__in=['pending', 'cooking', 'ready']
    ).prefetch_related('orderitem_set__pizza')
    
    completed_orders = Order.objects.filter(
        status='completed'
    ).prefetch_related('orderitem_set__pizza')
    
    context = {
        'active_orders': active_orders,
        'completed_orders': completed_orders,
    }
    
    active_orders_html = render_to_string('orders/active_orders.html', context)
    completed_orders_html = render_to_string('orders/completed_orders.html', context)
    
    return JsonResponse({
        'active_orders_html': active_orders_html,
        'completed_orders_html': completed_orders_html,
    })

def daily_report(request):
    today = timezone.now().date()
    daily_orders = Order.objects.filter(
        order_time__date=today
    ).prefetch_related('orderitem_set', 'orderitem_set__pizza', 'orderitem_set__pizza__ingredients')
    
    # Get all ingredients and initialize their usage
    ingredients = Ingredient.objects.all()
    items = []
    
    for ingredient in ingredients:
        used_amount = 0
        pizza_usage = []
        
        # Calculate usage from orders
        for order in daily_orders:
            for item in order.orderitem_set.all():
                if ingredient in item.pizza.ingredients.all():
                    used_amount += item.quantity
                    if item.pizza.name not in pizza_usage:
                        pizza_usage.append(item.pizza.name)
        
        current_stock = ingredient.current_stock
        items.append({
            'name': ingredient.name,
            'starting_stock': current_stock + used_amount,
            'used_today': used_amount,
            'current_stock': current_stock,
            'unit': ingredient.unit,
            'needs_reorder': current_stock <= ingredient.reorder_point,
            'running_low': current_stock <= ingredient.reorder_point * 2,
            'pizza_usage': pizza_usage
        })

    return render(request, 'orders/daily_report.html', {
        'items': items
    })