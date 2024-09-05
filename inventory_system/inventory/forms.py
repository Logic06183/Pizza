from django import forms
from .models import DailyStock, WeeklyStock, DailyStockRecord, WeeklyStockRecord, StockItem  # Use the correct models

class WeeklyStockForm(forms.ModelForm):
    class Meta:
        model = WeeklyStock
        exclude = ['date', 'items']  # Exclude fields like date and items to be handled in the view

class DailyStockForm(forms.ModelForm):
    class Meta:
        model = DailyStock
        exclude = ['date', 'items']  # Exclude fields like date and items

class StockRecordForm(forms.ModelForm):
    class Meta:
        model = DailyStockRecord  # or WeeklyStockRecord depending on which form
        fields = ['new_delivery', 'closing_stock', 'order_required']
