from django.test import TestCase
from orders.models import Pizza, PizzaOrder, PizzaOrderItem

class PizzaModelTest(TestCase):
    def test_string_representation(self):
        pizza = Pizza(name="Mushroom Cloud")
        self.assertEqual(str(pizza), "Mushroom Cloud")

class PizzaOrderModelTest(TestCase):
    def test_order_creation(self):
        pizza_order = PizzaOrder.objects.create(platform='Uber', preparation_time=30)
        self.assertEqual(pizza_order.platform, 'Uber')

class PizzaOrderItemModelTest(TestCase):
    def test_pizza_order_item_creation(self):
        pizza_order = PizzaOrder.objects.create(platform='Uber', preparation_time=30)
        pizza = Pizza.objects.create(name="Mushroom Cloud")
        order_item = PizzaOrderItem.objects.create(order=pizza_order, pizza_type=pizza, quantity=2)
        self.assertEqual(order_item.quantity, 2)
