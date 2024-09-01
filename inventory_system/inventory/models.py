from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WeeklyStock(models.Model):
    date = models.DateField()
    staff_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Weekly Stock on {self.date} by {self.staff_name}"

class DailyStock(models.Model):
    date = models.DateField()
    staff_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Daily Stock on {self.date} by {self.staff_name}"

class StockRecord(models.Model):
    stock = models.ForeignKey(WeeklyStock, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    new_delivery = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    order_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item.name} - {self.stock.date} ({self.stock.staff_name})"
    
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)  # Actual stock quantity

    def __str__(self):
        return self.name

