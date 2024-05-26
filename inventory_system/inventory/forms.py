from django import forms
from .models import WeeklyStock, Ingredient, DailyStock

class WeeklyStockForm(forms.ModelForm):
    class Meta:
        model = WeeklyStock
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DailyStockForm(forms.ModelForm):
    class Meta:
        model = DailyStock
        fields = '__all__'


