from django.db import models
from django.utils import timezone
from inventory.models import Ingredient
from datetime import timedelta

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, related_name='pizzas')
    description = models.TextField()  # Add this field
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    
    customer = models.CharField(max_length=100, default='Guest')
    date_created = models.DateTimeField(default=timezone.now)  # Changed from auto_now_add to default
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_time = models.DateTimeField(default=timezone.now)
    due_time = models.DateTimeField(null=True, blank=True)  # Make nullable initially
    completed_time = models.DateTimeField(null=True, blank=True)
    platform = models.CharField(max_length=100, choices=[
        ('web', 'Website'),
        ('app', 'Mobile App'),
    ], default='web')

    def save(self, *args, **kwargs):
        if not self.due_time:
            self.due_time = self.order_time + timedelta(minutes=45)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)  # Individual pizza notes

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} (Order #{self.order.id})"

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (R{self.price})"