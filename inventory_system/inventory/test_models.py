from django.test import TestCase
from inventory.models import Ingredient

class IngredientModelTest(TestCase):
    def test_string_representation(self):
        ingredient = Ingredient(name="Tomato")
        self.assertEqual(str(ingredient), "Tomato")

    def test_default_quantity(self):
        ingredient = Ingredient(name="Tomato")
        self.assertEqual(ingredient.quantity, 0)
