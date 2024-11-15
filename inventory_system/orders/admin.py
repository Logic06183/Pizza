from django.contrib import admin
from .models import Pizza, Order, OrderItem

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_created', 'status')
    list_filter = ('status', 'date_created')
    search_fields = ('customer',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'pizza', 'quantity')
    list_filter = ('pizza',)
    search_fields = ('order__id', 'pizza__name')
