from django.test import TestCase
from django.urls import reverse

class OrderListViewTest(TestCase):
    def test_order_list_view(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')
