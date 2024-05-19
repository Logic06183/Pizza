# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

