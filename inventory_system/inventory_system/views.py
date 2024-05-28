# inventory_system/views.py
from django.shortcuts import redirect

def redirect_to_orders(request):
    return redirect('order_list')
