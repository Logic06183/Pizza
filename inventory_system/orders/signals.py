# orders/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order, OrderItem
from inventory.models import DailyStock, WeeklyStock
from datetime import datetime, timedelta

@receiver(post_save, sender=Order)
def order_saved(sender, instance, created, **kwargs):
    if created:
        # Add any logic needed when a new order is created
        pass

@receiver(post_save, sender=OrderItem)
def order_item_saved(sender, instance, created, **kwargs):
    if created:
        # Update order total or handle inventory changes
        order = instance.order
        # Add your business logic here
        order.save()
