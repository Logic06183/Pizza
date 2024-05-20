from django.db import models

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
        ('Champ', 'Champ'),
        ('Pig n Paradise', 'Pig n Paradise'),
        ('Vegan Harvest', 'Vegan Harvest'),
        ('Mish-Mash', 'Mish-Mash'),
        ('Mushroom Cloud', 'Mushroom Cloud'),
        ('Feisty Italian', 'Feisty Italian'),
        ('Sausage Party', 'Sausage Party'),
        ('Zesty Zucchini', 'Zesty Zucchini'),
        ('Spud', 'Spud'),
        ('Owen', 'Owen'),
        ('Build Your Own', 'Build Your Own'),
        ('Lekkerizza Pizza', 'Lekkerizza Pizza'),
        ('Poppas Pizza', 'Poppas Pizza'),
        ('Sunshine Margherita', 'Sunshine Margherita'),
        ('Chick Tick Boom', 'Chick Tick Boom'),
        ('Ham & Artichoke', 'Ham & Artichoke'),
        ('Veg Special', 'Veg Special'),
        ('Janes Dough', 'Janes Dough'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    pizza_type = models.JSONField(default=list)  # Updated to list
    extra_toppings = models.TextField(blank=True)
    preparation_time = models.IntegerField(help_text="Time in minutes")
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order on {self.platform} at {self.order_time}"

