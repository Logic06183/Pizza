# inventory/urls.py
from django.urls import path
from .views import inventory_list, add_item

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('add/', add_item, name='add_item'),
]

