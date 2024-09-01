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
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    extra_toppings = models.TextField(blank=True)
    preparation_time = models.IntegerField(help_text="Time in minutes")
    order_time = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=True)  # Field to control display of the order

    def __str__(self):
        return f"Order on {self.platform} at {self.order_time}"

    def calculate_ingredient_usage(self):
        total_usage = {}
        for item in self.pizzaorderitem_set.all():
            pizza = item.pizza_type
            quantity = item.quantity
            pizza_ingredients = PizzaIngredient.objects.filter(pizza=pizza)
            for pi in pizza_ingredients:
                ingredient = pi.ingredient.name
                amount = pi.quantity_needed
                if ingredient not in total_usage:
                    total_usage[ingredient] = 0
                total_usage[ingredient] += amount * quantity
        return total_usage

class PizzaOrderItem(models.Model):
    order = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE)
    pizza_type = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.pizza_type.name} for order {self.order_id}"
