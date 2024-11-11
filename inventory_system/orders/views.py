from django.shortcuts import render, redirect
from .models import Order, Pizza, OrderItem  # Updated imports
from .forms import OrderForm  # Remove PizzaOrderForm
from inventory.models import Ingredient  # This import should now work correctly
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

def add_order(request):
    pizzas = Pizza.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                # Create order
                order = form.save(commit=False)
                order.save()

                # Process pizza quantities
                has_pizzas = False
                for pizza in pizzas:
                    quantity = int(request.POST.get(f'quantity_{pizza.id}', 0))
                    if quantity > 0:
                        OrderItem.objects.create(
                            order=order,
                            pizza=pizza,
                            quantity=quantity
                        )
                        has_pizzas = True

                if not has_pizzas:
                    order.delete()
                    messages.error(request, 'Please add at least one pizza to the order.')
                    return render(request, 'orders/add_order.html', {'form': form, 'pizzas': pizzas})

                messages.success(request, 'Order created successfully!')
                return redirect('order_list')

            except Exception as e:
                messages.error(request, f'Error creating order: {str(e)}')
                return render(request, 'orders/add_order.html', {'form': form, 'pizzas': pizzas})
    else:
        form = OrderForm()

    return render(request, 'orders/add_order.html', {'form': form, 'pizzas': pizzas})


def order_list(request):
    active_orders = Order.objects.filter(status__in=['pending', 'cooking', 'ready']).order_by('due_time')
    completed_orders = Order.objects.filter(status='completed').order_by('-completed_time')
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
    active_orders = Order.objects.filter(status__in=['pending', 'cooking', 'ready']).order_by('due_time')
    completed_orders = Order.objects.filter(status='completed').order_by('-completed_time')
    active_orders_html = render_to_string('orders/active_orders.html', {'active_orders': active_orders})
    completed_orders_html = render_to_string('orders/completed_orders.html', {'completed_orders': completed_orders})
    return JsonResponse({
        'active_orders_html': active_orders_html,
        'completed_orders_html': completed_orders_html,
    })

def daily_report(request):
    today = timezone.now().date()
    daily_orders = Order.objects.filter(order_time__date=today)
    
    # Initialize ingredient totals
    ingredient_usage = {}
    
    # Calculate ingredient usage from orders
    for order in daily_orders:
        pizza_type = order.pizza_type
        if pizza_type in PIZZA_INGREDIENTS:
            for ingredient, amount in PIZZA_INGREDIENTS[pizza_type].items():
                if ingredient not in ingredient_usage:
                    ingredient_usage[ingredient] = 0
                ingredient_usage[ingredient] += amount * order.quantity

    # Get current stock levels (assuming you have a Stock model)
    stock_items = []
    for ingredient, used_amount in ingredient_usage.items():
        current_stock = Stock.objects.get(name=ingredient).quantity
        stock_items.append({
            'name': ingredient,
            'current_stock': current_stock,
            'estimated_usage': used_amount,
            'estimated_remaining': current_stock - used_amount
        })

    return render(request, 'orders/daily_report.html', {'items': stock_items})

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