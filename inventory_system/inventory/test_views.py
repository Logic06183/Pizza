from django.test import TestCase
from django.urls import reverse
from .models import WeeklyStock, DailyStock, StockItem, StockRecord

class StockViewTests(TestCase):

    def setUp(self):
        # Create a couple of stock items to use in the tests
        self.item1 = StockItem.objects.create(name='Item 1')
        self.item2 = StockItem.objects.create(name='Item 2')

    def test_add_weekly_stock_valid_data(self):
        response = self.client.post(reverse('add_weekly_stock'), {
            'date': '2024-09-01',
            'staff_name': 'Test Staff',
            f'new_delivery_{self.item1.id}': 10,
            f'closing_stock_{self.item1.id}': 5,
            f'order_required_{self.item1.id}': False,
            f'new_delivery_{self.item2.id}': 20,
            f'closing_stock_{self.item2.id}': 10,
            f'order_required_{self.item2.id}': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(WeeklyStock.objects.count(), 1)
        self.assertEqual(StockRecord.objects.count(), 2)

    def test_add_daily_stock_valid_data(self):
        response = self.client.post(reverse('add_daily_stock'), {
            'date': '2024-09-01',
            'staff_name': 'Test Staff',
            f'new_delivery_{self.item1.id}': 10,
            f'closing_stock_{self.item1.id}': 5,
            f'order_required_{self.item1.id}': False,
            f'new_delivery_{self.item2.id}': 20,
            f'closing_stock_{self.item2.id}': 10,
            f'order_required_{self.item2.id}': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(DailyStock.objects.count(), 1)
        self.assertEqual(StockRecord.objects.count(), 2)

