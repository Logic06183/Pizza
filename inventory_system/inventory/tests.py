from django.test import TestCase
from inventory.models import WeeklyStock, DailyStock, Ingredient, Pizza, PizzaIngredient
from django.urls import reverse

class WeeklyStockModelTest(TestCase):
    def test_create_weekly_stock(self):
        weekly_stock = WeeklyStock.objects.create(
            date='2024-08-31',
            staff_name='John Doe',
            pizza_box_new_delivery=10,
            pizza_box_closing_stock=5,
            pizza_box_order_required=True,
            cooking_oil_new_delivery=8,
            cooking_oil_closing_stock=2,
            cooking_oil_order_required=True,
        )
        self.assertEqual(weekly_stock.pizza_box_new_delivery, 10)
        self.assertTrue(weekly_stock.pizza_box_order_required)

class DailyStockModelTest(TestCase):
    def test_create_daily_stock(self):
        daily_stock = DailyStock.objects.create(
            date='2024-08-31',
            staff_name='Jane Doe',
            dough_balls_new_delivery=20,
            dough_balls_closing_stock=10,
            dough_balls_order_required=False,
        )
        self.assertEqual(daily_stock.dough_balls_new_delivery, 20)
        self.assertFalse(daily_stock.dough_balls_order_required)

class IngredientModelTest(TestCase):
    def test_create_ingredient(self):
        ingredient = Ingredient.objects.create(name='Mozzarella', quantity=100)
        self.assertEqual(ingredient.name, 'Mozzarella')
        self.assertEqual(ingredient.quantity, 100)

class PizzaModelTest(TestCase):
    def test_create_pizza_with_ingredients(self):
        mozzarella = Ingredient.objects.create(name='Mozzarella', quantity=100)
        tomato_sauce = Ingredient.objects.create(name='Tomato Sauce', quantity=50)
        
        pizza = Pizza.objects.create(name='Margherita')
        PizzaIngredient.objects.create(pizza=pizza, ingredient=mozzarella, quantity_needed=50)
        PizzaIngredient.objects.create(pizza=pizza, ingredient=tomato_sauce, quantity_needed=20)
        
        self.assertEqual(pizza.ingredients.count(), 2)

class PizzaViewTest(TestCase):
    def test_pizza_list_view(self):
        response = self.client.get(reverse('pizza_list'))  # Assuming there's a view named 'pizza_list'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")

class IngredientViewTest(TestCase):
    def test_ingredient_list_view(self):
        response = self.client.get(reverse('ingredient_list'))  # Assuming there's a view named 'ingredient_list'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ingredient")
