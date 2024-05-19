from django import forms
from .models import WeeklyStock, Ingredient

class WeeklyStockForm(forms.ModelForm):
    class Meta:
        model = WeeklyStock
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

