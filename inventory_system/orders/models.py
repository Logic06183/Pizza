# orders/models.py
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)  # Actual stock quantity

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='PizzaIngredient')

    def __str__(self):
        return self.name

class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.FloatField(default=0)  # Quantity needed for this pizza (in grams, for example)

class PizzaOrder(models.Model):
    PLATFORM_CHOICES = [
        ('Uber', 'Uber'),
        ('Mr Delivery', 'Mr Delivery'),
        ('Bolt', 'Bolt'),
        ('Window', 'Window'),
        ('Other', 'Other'),
    ]
    PIZZA_CHOICES = [
        ('Margie', 'Margie'),
        ('Sunshine Margherita', 'Sunshine Margherita'),
        ('Spud', 'Spud'),
        ('Zesty Zucchini', 'Zesty Zucchini'),
        ('Mushroom Cloud', 'Mushroom Cloud'),
        ('Vegan Harvest', 'Vegan Harvest'),
        ('Jane\'s Dough', 'Jane\'s Dough'),
        ('The Champ', 'The Champ'),
        ('Mish-Mash', 'Mish-Mash'),
        ('Pig in Paradise', 'Pig in Paradise'),
        ('Poppa\'s Pizza', 'Poppa\'s Pizza'),
        ('Lekkerízza', 'Lekkerízza'),
        ('Artichoke & Ham', 'Artichoke & Ham'),
        ('Chick Tick Boom', 'Chick Tick Boom'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    pizza_type = models.JSONField(default=list)  # List of pizza names
    quantities = models.JSONField(default=list)  # List of quantities corresponding to each pizza
    extra_toppings = models.TextField(blank=True)
    preparation_time = models.IntegerField(help_text="Time in minutes")
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order on {self.platform} at {self.order_time}"

    def calculate_ingredient_usage(self):
        total_usage = {}
        for pizza_name, quantity in zip(self.pizza_type, self.quantities):
            try:
                pizza = Pizza.objects.get(name=pizza_name)
            except Pizza.DoesNotExist:
                continue
            pizza_ingredients = PizzaIngredient.objects.filter(pizza=pizza)
            for pi in pizza_ingredients:
                ingredient = pi.ingredient.name
                amount = pi.quantity_needed
                if ingredient not in total_usage:
                    total_usage[ingredient] = 0
                total_usage[ingredient] += amount * int(quantity)
        return total_usage
