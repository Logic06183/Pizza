from django.test import TestCase
from django.urls import reverse

class WeeklyStockListViewTest(TestCase):
    def test_weekly_stock_list_view(self):
        response = self.client.get(reverse('weekly_stock_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/weekly_stock_list.html')
