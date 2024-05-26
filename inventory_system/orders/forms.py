from django import forms
from .models import PizzaOrder

PIZZA_CHOICES = [
    ('Margie', 'Margie'),
    ('Champ', 'Champ'),
    ('Pig n Paradise', 'Pig n Paradise'),
    ('Vegan Harvest', 'Vegan Harvest'),
    ('Mish-Mash', 'Mish-Mash'),
    ('Mushroom Cloud', 'Mushroom Cloud'),
    ('Feisty Italian', 'Feisty Italian'),
    ('Sausage Party', 'Sausage Party'),
    ('Zesty Zucchini', 'Zesty Zucchini'),
    ('Spud', 'Spud'),
    ('Owen', 'Owen'),
    ('Build Your Own', 'Build Your Own'),
    ('Lekkerizza Pizza', 'Lekkerizza Pizza'),
    ('Poppas Pizza', 'Poppas Pizza'),
    ('Sunshine Margherita', 'Sunshine Margherita'),
    ('Chick Tick Boom', 'Chick Tick Boom'),
    ('Ham & Artichoke', 'Ham & Artichoke'),
    ('Veg Special', 'Veg Special'),
    ('Janes Dough', 'Janes Dough'),
]

class PizzaOrderForm(forms.ModelForm):
    pizza_type = forms.MultipleChoiceField(choices=PIZZA_CHOICES, widget=forms.CheckboxSelectMultiple, required=True)
    quantities = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}), help_text="Enter quantities as comma-separated values corresponding to selected pizzas")

    class Meta:
        model = PizzaOrder
        fields = ['platform', 'pizza_type', 'quantities', 'extra_toppings', 'preparation_time']

    def clean_quantities(self):
        quantities = self.cleaned_data['quantities']
        quantities_list = quantities.split(',')
        if len(quantities_list) != len(self.cleaned_data['pizza_type']):
            raise forms.ValidationError("Each selected pizza must have a corresponding quantity.")
        return quantities_list
