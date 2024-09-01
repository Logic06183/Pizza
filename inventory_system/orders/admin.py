# orders/admin.py

from django.contrib import admin
from .models import Pizza, PizzaOrder, PizzaOrderItem

# Register the Pizza model
admin.site.register(Pizza)
admin.site.register(PizzaOrder)
admin.site.register(PizzaOrderItem)

