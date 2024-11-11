from django.db import models
from django.utils import timezone

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('cooking', 'Cooking'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_time = models.DateTimeField(default=timezone.now)
    due_time = models.DateTimeField()
    completed_time = models.DateTimeField(null=True, blank=True)
    platform = models.CharField(max_length=50)
    preparation_time = models.IntegerField(default=30)
    extra_toppings = models.TextField(blank=True)
    
    @property
    def is_high_priority(self):
        return (self.due_time - timezone.now()).total_seconds() < 900  # 15 minutes

    @property
    def is_almost_due(self):
        return (self.due_time - timezone.now()).total_seconds() < 1800  # 30 minutes

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} for Order #{self.order.id}"