from django.shortcuts import render, redirect
from .models import PizzaOrder
from .forms import PizzaOrderForm
from datetime import datetime, timedelta
import pytz

def add_order(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.pizza_type = form.cleaned_data['pizza_type']
            pizza_order.save()
            return redirect('order_list')
    else:
        form = PizzaOrderForm()
    return render(request, 'orders/add_order.html', {'form': form})

def order_list(request):
    orders = PizzaOrder.objects.all().order_by('order_time')
    current_time = datetime.now(pytz.timezone('Africa/Johannesburg'))  # Use timezone-aware datetime
    for order in orders:
        order.due_time = order.order_time + timedelta(minutes=order.preparation_time)
        order.is_late = current_time > order.due_time
        order.is_high_priority = current_time + timedelta(minutes=5) > order.due_time and not order.is_late
    return render(request, 'orders/order_list.html', {'orders': orders})



