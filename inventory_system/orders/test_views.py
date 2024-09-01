from django.test import TestCase
from django.urls import reverse
from .models import PizzaOrder, PizzaOrderItem, Pizza

class OrderListViewTests(TestCase):

    def setUp(self):
        # Setup for today's order
        self.today_order = PizzaOrder.objects.create(
            platform='Uber', 
            extra_toppings='Extra cheese',
            preparation_time=10,
        )
        self.pizza1 = Pizza.objects.create(name='Margarita')
        self.pizza2 = Pizza.objects.create(name='Pepperoni')
        PizzaOrderItem.objects.create(order=self.today_order, pizza_type=self.pizza1, quantity=2)
        PizzaOrderItem.objects.create(order=self.today_order, pizza_type=self.pizza2, quantity=1)

        # Setup for a past order
        self.past_order = PizzaOrder.objects.create(
            platform='Bolt', 
            extra_toppings='Olives',
            preparation_time=15,
        )
        PizzaOrderItem.objects.create(order=self.past_order, pizza_type=self.pizza1, quantity=3)

    def test_order_list_view_displays_pizza_types_and_quantities(self):
        response = self.client.get(reverse('order_list'))
        self.assertContains(response, 'Margarita')
        self.assertContains(response, 'Pepperoni')
        self.assertContains(response, '2')
        self.assertContains(response, '1')
    
    def test_order_list_view_displays_only_today_orders(self):
        response = self.client.get(reverse('order_list'))
        self.assertContains(response, 'Uber')
        self.assertNotContains(response, 'Bolt')
