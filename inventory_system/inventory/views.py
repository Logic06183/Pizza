# inventory/views.py
from django.shortcuts import render, redirect
from .models import InventoryItem
from .forms import InventoryItemForm

def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})


# Create your views here.
