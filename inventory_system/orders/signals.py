# orders/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PizzaOrder
from inventory.models import DailyStock, WeeklyStock
from datetime import datetime, timedelta

@receiver(post_save, sender=PizzaOrder)
def update_stock(sender, instance, created, **kwargs):
    if created:
        date_today = datetime.today().date()
        
        # Update daily stock
        daily_stock, created = DailyStock.objects.get_or_create(date=date_today, staff_name="Automated System")
        
        usage = instance.calculate_ingredient_usage()
        for ingredient, amount in usage.items():
            new_delivery_field = f"{ingredient}_new_delivery"
            closing_stock_field = f"{ingredient}_closing_stock"
            
            if hasattr(daily_stock, new_delivery_field):
                setattr(daily_stock, new_delivery_field, getattr(daily_stock, new_delivery_field) + amount)
            if hasattr(daily_stock, closing_stock_field):
                setattr(daily_stock, closing_stock_field, getattr(daily_stock, closing_stock_field) - amount)
        
        daily_stock.save()

        # Update weekly stock
        start_of_week = date_today - timedelta(days=date_today.weekday())
        weekly_stock, created = WeeklyStock.objects.get_or_create(date=start_of_week, staff_name="Automated System")
        
        for ingredient, amount in usage.items():
            new_delivery_field = f"{ingredient}_new_delivery"
            closing_stock_field = f"{ingredient}_closing_stock"
            
            if hasattr(weekly_stock, new_delivery_field):
                setattr(weekly_stock, new_delivery_field, getattr(weekly_stock, new_delivery_field) + amount)
            if hasattr(weekly_stock, closing_stock_field):
                setattr(weekly_stock, closing_stock_field, getattr(weekly_stock, closing_stock_field) - amount)
        
        weekly_stock.save()
