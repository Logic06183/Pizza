from django.shortcuts import render, redirect
from .models import PizzaOrder, Pizza, PizzaOrderItem
from .forms import PizzaOrderForm
from inventory.models import Ingredient  # This import should now work correctly
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json

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
    active_orders = Order.objects.filter(status__in=['new', 'cooking', 'ready']).order_by('due_time')
    completed_orders = Order.objects.filter(status='completed').order_by('-completed_time')[:10]
    
    return render(request, 'orders/order_list.html', {
        'active_orders': active_orders,
        'completed_orders': completed_orders,
    })

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
    active_orders = Order.objects.filter(status__in=['new', 'cooking', 'ready']).order_by('due_time')
    completed_orders = Order.objects.filter(status='completed').order_by('-completed_time')[:10]
    
    active_orders_html = render_to_string('orders/partials/active_orders.html', {'active_orders': active_orders})
    completed_orders_html = render_to_string('orders/partials/completed_orders.html', {'completed_orders': completed_orders})
    
    return JsonResponse({
        'active_orders_html': active_orders_html,
        'completed_orders_html': completed_orders_html
    })

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

# orders/views.py
from django.shortcuts import render
from .models import Order  # Add this import

def order_list(request):
    active_orders = Order.objects.filter(
        status__in=['new', 'cooking', 'ready']
    ).order_by('due_time')
    
    completed_orders = Order.objects.filter(
        status='delivered'
    ).order_by('-due_time')
    
    context = {
        'active_orders': active_orders,
        'completed_orders': completed_orders
    }
    return render(request, 'orders/order_list.html', context)