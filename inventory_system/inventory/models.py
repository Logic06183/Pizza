from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WeeklyStock(models.Model):
    date = models.DateField(auto_now_add=True)

class DailyStock(models.Model):
    date = models.DateField(auto_now_add=True)


class StockRecord(models.Model):
    stock = models.ForeignKey(WeeklyStock, on_delete=models.CASCADE)  # Or DailyStock, depending on context
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    new_delivery = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    order_required = models.BooleanField(default=False)
