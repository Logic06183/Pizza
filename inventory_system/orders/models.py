from django.db import models
from django.utils import timezone
from inventory.models import Ingredient

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, related_name='pizzas')
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('cooking', 'Cooking'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]
    PLATFORM_CHOICES = [
        ('Uber', 'Uber'),
        ('Bolt', 'Bolt'),
        ('Window', 'Window'),
    ]
    
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_time = models.DateTimeField(default=timezone.now)
    due_time = models.DateTimeField(null=True, blank=True)
    completed_time = models.DateTimeField(null=True, blank=True)
    extra_toppings = models.TextField(blank=True)
    preparation_time = models.IntegerField(default=30)  # in minutes
    notes = models.TextField(blank=True)  # General order notes

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)  # Individual pizza notes

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} (Order #{self.order.id})"