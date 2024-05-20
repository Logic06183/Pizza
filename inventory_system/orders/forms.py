from django import forms
from .models import PizzaOrder

class PizzaOrderForm(forms.ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['platform', 'pizza_type', 'extra_toppings', 'preparation_time']
        widgets = {
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'pizza_type': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'extra_toppings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }


