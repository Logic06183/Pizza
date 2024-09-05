from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StockItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class DailyStock(models.Model):
    date = models.DateField(auto_now_add=True)
    staff_name = models.CharField(max_length=100, default="Unknown")
    items = models.ManyToManyField(StockItem, through='DailyStockRecord')

    def __str__(self):
        return f"Daily Stock - {self.date} by {self.staff_name}"

class WeeklyStock(models.Model):
    date = models.DateField(auto_now_add=True)
    staff_name = models.CharField(max_length=100, default="Unknown")
    items = models.ManyToManyField(StockItem, through='WeeklyStockRecord')

    def __str__(self):
        return f"Weekly Stock - {self.date} by {self.staff_name}"

class DailyStockRecord(models.Model):
    stock = models.ForeignKey(DailyStock, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    new_delivery = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    order_required = models.BooleanField(default=False)

class WeeklyStockRecord(models.Model):
    stock = models.ForeignKey(WeeklyStock, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    new_delivery = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    order_required = models.BooleanField(default=False)
