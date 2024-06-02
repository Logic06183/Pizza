# orders/management/commands/clear_orders.py

from django.core.management.base import BaseCommand
from orders.models import PizzaOrder

class Command(BaseCommand):
    help = 'Clear the order list at the end of each day'

    def handle(self, *args, **kwargs):
        PizzaOrder.objects.update(display=False)
        self.stdout.write(self.style.SUCCESS('Successfully cleared the order list'))
