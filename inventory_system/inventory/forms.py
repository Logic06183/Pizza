from django import forms
from .models import WeeklyStock, DailyStock, StockItem, StockRecord

class WeeklyStockForm(forms.ModelForm):
    class Meta:
        model = WeeklyStock
        fields = ['date', 'staff_name']

class DailyStockForm(forms.ModelForm):
    class Meta:
        model = DailyStock
        fields = ['date', 'staff_name']

class StockRecordForm(forms.ModelForm):
    class Meta:
        model = StockRecord
        fields = ['new_delivery', 'closing_stock', 'order_required']
