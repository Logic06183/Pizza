from django import forms
from .models import PizzaOrder, Pizza

class PizzaOrderForm(forms.ModelForm):
    pizza_type = forms.ModelMultipleChoiceField(
        queryset=Pizza.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True
    )
    
    class Meta:
        model = PizzaOrder
        fields = ['platform', 'pizza_type', 'extra_toppings', 'preparation_time']

    def __init__(self, *args, **kwargs):
        super(PizzaOrderForm, self).__init__(*args, **kwargs)
        pizzas = Pizza.objects.all()
        for pizza in pizzas:
            self.fields[f'quantity_{pizza.id}'] = forms.IntegerField(
                label=f'{pizza.name} Quantity', 
                min_value=0, 
                required=False,
                initial=0,
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )

    def clean(self):
        cleaned_data = super().clean()
        total_quantity = 0
        for key, value in cleaned_data.items():
            if key.startswith('quantity_') and value:
                total_quantity += value
        if total_quantity == 0:
            raise forms.ValidationError("You must order at least one pizza.")
        return cleaned_data
