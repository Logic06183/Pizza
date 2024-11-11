from django.db import models
from django.utils import timezone

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    ingredients = models.ManyToManyField('inventory.Ingredient')  # Remove blank=True for now

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('cooking', 'Cooking'),
        ('ready', 'Ready'),
        ('completed', 'Completed')
    ]
    
    platform = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_time = models.DateTimeField(default=timezone.now)
    completed_time = models.DateTimeField(null=True, blank=True)
    due_time = models.DateTimeField(null=True, blank=True)
    extra_toppings = models.TextField(blank=True)
    preparation_time = models.IntegerField(default=30)  # in minutes

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} for Order #{self.order.id}"