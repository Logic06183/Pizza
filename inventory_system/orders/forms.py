from django import forms
from .models import PizzaOrder, Pizza  # Import the Pizza model

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
from django import forms
from .models import PizzaOrder, Pizza

class PizzaOrderForm(forms.ModelForm):
    pizza_type = forms.ModelMultipleChoiceField(
        queryset=Pizza.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # You can use a checkbox widget or a select multiple widget
        required=True
    )

    class Meta:
        model = PizzaOrder
        fields = ['platform', 'pizza_type', 'extra_toppings', 'preparation_time']


