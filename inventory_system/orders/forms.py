# orders/forms.py

from django import forms
from .models import Order, OrderItem, Pizza  # Fixed imports to match actual model names
from django.utils import timezone
from datetime import timedelta

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['platform', 'extra_toppings', 'preparation_time']
        widgets = {
            'extra_toppings': forms.Textarea(attrs={'rows': 3}),
            'preparation_time': forms.NumberInput(attrs={'min': 1})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('due_time'):
            self.initial['due_time'] = timezone.now() + timedelta(minutes=30)

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['pizza', 'quantity', 'notes']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }




