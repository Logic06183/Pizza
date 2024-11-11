# orders/forms.py

from django import forms
from .models import PizzaOrder, PizzaOrderItem, Pizza, Order
from django.utils import timezone
from datetime import timedelta

class PizzaOrderForm(forms.ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['platform', 'extra_toppings', 'preparation_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically add a field for each pizza type
        for pizza in Pizza.objects.all():
            self.fields[f'pizza_{pizza.id}'] = forms.IntegerField(
                label=f'{pizza.name} Quantity',
                min_value=0,
                required=False,
                initial=0,
            )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['platform', 'due_time', 'extra_toppings', 'preparation_time']
        widgets = {
            'due_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('due_time'):
            self.initial['due_time'] = timezone.now() + timedelta(minutes=30)




