from django import forms
from .models import WeeklyStock, DailyStock, StockRecord

class WeeklyStockForm(forms.ModelForm):
    class Meta:
        model = WeeklyStock
        exclude = ['date']  # Exclude the date field as it is non-editable

class DailyStockForm(forms.ModelForm):
    class Meta:
        model = DailyStock
        exclude = ['date']  # Exclude the date field as it is non-editable

class StockRecordForm(forms.ModelForm):
    class Meta:
        model = StockRecord
        fields = ['new_delivery', 'closing_stock', 'order_required']  # Add relevant fields
