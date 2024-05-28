from django.core.management.base import BaseCommand
from inventory.models import Pizza, Ingredient, PizzaIngredient

class Command(BaseCommand):
    help = 'Populate pizzas and their ingredients'

    def handle(self, *args, **kwargs):
        # Define pizza ingredients and quantities
        pizza_data = {
            'Margie': {'dough': 1, 'pizza_sauce': 1, 'fresh_mozzarella': 20, 'basil': 10, 'olive_oil': 5},
            'Sunshine Margherita': {'dough': 1, 'pesto_sauce': 1, 'ricotta': 20, 'sundried_tomato': 10, 'basil': 10, 'olive_oil': 5},
            'Spud': {'dough': 1, 'shredded_cheese': 20, 'parmesan': 10, 'cooked_potato': 15, 'caramelised_onion': 10, 'chilli_oil': 5},
            'Zesty Zucchini': {'dough': 1, 'fresh_mozzarella': 20, 'blue_cheese': 10, 'parmesan': 10, 'zucchini': 15, 'basil': 10, 'olive_oil': 5},
            'Mushroom Cloud': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'goat_cheese': 10, 'mushroom': 15, 'caramelised_onion': 10, 'sunflower_seeds': 5, 'chilli_oil': 5},
            'Vegan Harvest': {'dough': 1, 'pizza_sauce': 1, 'mushroom': 15, 'sundried_tomato': 10, 'olives': 10, 'zucchini': 15, 'rocket': 10, 'olive_oil': 5, 'hummus': 5},
            'Janes Dough': {'dough': 1, 'olives': 10, 'rocket': 10, 'olive_oil': 5},
            'Champ': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'spring_onion': 10, 'pepperoni': 15, 'olive_oil': 5},
            'Mish-Mash': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'goat_cheese': 10, 'rocket': 10, 'parma_ham': 15, 'fig_jam': 5},
            'Pig n Paradise': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'cooked_pineapple': 10, 'bacon': 15},
            'Poppas Pizza': {'dough': 1, 'pizza_sauce': 1, 'fresh_mozzarella': 20, 'olives': 10, 'basil': 10, 'anchovies': 10, 'olive_oil': 5},
            'Lekkerizza Pizza': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'feta': 10, 'peppadew': 10, 'rocket': 10, 'chorizo': 15, 'bacon': 15},
            'Ham & Artichoke': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'artichoke_leaves': 10, 'olives': 10, 'mushroom': 15, 'ham': 15},
            'Chick Tick Boom': {'dough': 1, 'pizza_sauce': 1, 'shredded_cheese': 20, 'peppadew': 10, 'coriander': 10, 'cooked_chicken': 15},
        }

        for pizza_name, ingredients in pizza_data.items():
            pizza, created = Pizza.objects.get_or_create(name=pizza_name)
            for ingredient_name, quantity_needed in ingredients.items():
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                PizzaIngredient.objects.get_or_create(pizza=pizza, ingredient=ingredient, defaults={'quantity_needed': quantity_needed})

        self.stdout.write(self.style.SUCCESS('Successfully populated pizzas and ingredients.'))
