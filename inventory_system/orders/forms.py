from django import forms
from .models import PizzaOrder

class PizzaOrderForm(forms.ModelForm):
    pizza_type = forms.MultipleChoiceField(
        choices=PizzaOrder.PIZZA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Pizza Types'
    )

    class Meta:
        model = PizzaOrder
        fields = ['platform', 'pizza_type', 'extra_toppings', 'preparation_time']
        widgets = {
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'extra_toppings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }
