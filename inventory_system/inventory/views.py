from django.shortcuts import render, redirect
from .models import WeeklyStock, DailyStock, StockItem, StockRecord
from .forms import WeeklyStockForm, DailyStockForm, StockRecordForm
from django.db import transaction

# Utility function to handle stock forms (both weekly and daily)
def handle_stock_form(request, stock_form_class, template_name, redirect_name):
    stock_items = StockItem.objects.all()
    if request.method == 'POST':
        stock_form = stock_form_class(request.POST)
        if stock_form.is_valid():
            with transaction.atomic():
                stock_instance = stock_form.save()

                stock_records = []
                for item in stock_items:
                    stock_record_form = StockRecordForm({
                        'new_delivery': request.POST.get(f'new_delivery_{item.id}', 0),
                        'closing_stock': request.POST.get(f'closing_stock_{item.id}', 0),
                        'order_required': request.POST.get(f'order_required_{item.id}', False),
                    })
                    if stock_record_form.is_valid():
                        stock_record = stock_record_form.save(commit=False)
                        stock_record.stock = stock_instance
                        stock_record.item = item
                        stock_records.append(stock_record)

                StockRecord.objects.bulk_create(stock_records)
            return redirect(redirect_name)
    else:
        stock_form = stock_form_class()

    return render(request, template_name, {
        'form': stock_form,
        'stock_items': stock_items,
    })

# View to add weekly stock
def add_weekly_stock(request):
    return handle_stock_form(request, WeeklyStockForm, 'inventory/add_weekly_stock.html', 'weekly_stock_list')

# View to add daily stock
def add_daily_stock(request):
    return handle_stock_form(request, DailyStockForm, 'inventory/add_daily_stock.html', 'daily_stock_list')

# View to list all stocks
def stock_list(request):
    stocks = StockItem.objects.all()
    return render(request, 'inventory/stock_list.html', {'stocks': stocks})

# View to list all daily stocks
def daily_stock_list(request):
    stocks = DailyStock.objects.all()
    return render(request, 'inventory/daily_stock_list.html', {'stocks': stocks})

# View to list all weekly stocks
def weekly_stock_list(request):
    stocks = WeeklyStock.objects.all()
    return render(request, 'inventory/weekly_stock_list.html', {'stocks': stocks})

from django.shortcuts import render
from .models import WeeklyStock

def weekly_stock_report(request):
    stocks = WeeklyStock.objects.all()
    return render(request, 'inventory/weekly_stock_report.html', {'stocks': stocks})
