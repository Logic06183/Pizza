from django.shortcuts import render, redirect
from django.db import transaction
from .models import WeeklyStock, DailyStock, StockItem, WeeklyStockRecord, DailyStockRecord
from .forms import WeeklyStockForm, DailyStockForm

def add_weekly_stock(request):
    stock_items = StockItem.objects.all()  # Fetch stock items
    if request.method == 'POST':
        form = WeeklyStockForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                weekly_stock = form.save()

                # Process each stock item input
                for item in stock_items:
                    new_delivery = request.POST.get(f'new_delivery_{item.id}', 0)
                    closing_stock = request.POST.get(f'closing_stock_{item.id}', 0)
                    order_required = request.POST.get(f'order_required_{item.id}', 'off') == 'on'

                    if int(new_delivery) > 0 or int(closing_stock) > 0:
                        WeeklyStockRecord.objects.create(
                            stock=weekly_stock,
                            item=item,
                            new_delivery=int(new_delivery),
                            closing_stock=int(closing_stock),
                            order_required=order_required
                        )

            return redirect('weekly_stock_list')  # Redirect after form submission
    else:
        form = WeeklyStockForm()

    return render(request, 'inventory/add_weekly_stock.html', {'form': form, 'stock_items': stock_items})

def add_daily_stock(request):
    stock_items = StockItem.objects.all()  # Fetch stock items
    if request.method == 'POST':
        form = DailyStockForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                daily_stock = form.save()

                # Process each stock item input
                for item in stock_items:
                    new_delivery = request.POST.get(f'new_delivery_{item.id}', 0)
                    closing_stock = request.POST.get(f'closing_stock_{item.id}', 0)
                    order_required = request.POST.get(f'order_required_{item.id}', 'off') == 'on'

                    if int(new_delivery) > 0 or int(closing_stock) > 0:
                        DailyStockRecord.objects.create(
                            stock=daily_stock,
                            item=item,
                            new_delivery=int(new_delivery),
                            closing_stock=int(closing_stock),
                            order_required=order_required
                        )

            return redirect('daily_stock_list')  # Redirect after form submission
    else:
        form = DailyStockForm()

    return render(request, 'inventory/add_daily_stock.html', {'form': form, 'stock_items': stock_items})

from django.shortcuts import render
from .models import WeeklyStock, WeeklyStockRecord

def weekly_stock_list(request):
    stocks = WeeklyStockRecord.objects.all()  # Fetch all weekly stock records
    return render(request, 'inventory/weekly_stock_list.html', {'stocks': stocks})

from django.shortcuts import render
from .models import DailyStockRecord

def daily_stock_list(request):
    stocks = DailyStockRecord.objects.all()  # Fetch all daily stock records
    return render(request, 'inventory/daily_stock_list.html', {'stocks': stocks})

from django.shortcuts import render
from .models import WeeklyStockRecord, DailyStockRecord

# View to generate weekly stock report
def weekly_stock_report(request):
    weekly_stocks = WeeklyStockRecord.objects.all()
    return render(request, 'inventory/weekly_stock_report.html', {'stocks': weekly_stocks})

# View to generate daily stock report
def daily_stock_report(request):
    daily_stocks = DailyStockRecord.objects.all()
    return render(request, 'inventory/daily_stock_report.html', {'stocks': daily_stocks})

