from django.db import models

class WeeklyStock(models.Model):
    date = models.DateField()
    staff_name = models.CharField(max_length=100)
    pizza_box_new_delivery = models.IntegerField(default=0)
    pizza_box_closing_stock = models.IntegerField(default=0)
    pizza_box_order_required = models.BooleanField(default=False)
    cooking_oil_new_delivery = models.IntegerField(default=0)
    cooking_oil_closing_stock = models.IntegerField(default=0)
    cooking_oil_order_required = models.BooleanField(default=False)
    salt_new_delivery = models.IntegerField(default=0)
    salt_closing_stock = models.IntegerField(default=0)
    salt_order_required = models.BooleanField(default=False)
    sugar_new_delivery = models.IntegerField(default=0)
    sugar_closing_stock = models.IntegerField(default=0)
    sugar_order_required = models.BooleanField(default=False)
    dishwashing_liquid_new_delivery = models.IntegerField(default=0)
    dishwashing_liquid_closing_stock = models.IntegerField(default=0)
    dishwashing_liquid_order_required = models.BooleanField(default=False)
    bleach_new_delivery = models.IntegerField(default=0)
    bleach_closing_stock = models.IntegerField(default=0)
    bleach_order_required = models.BooleanField(default=False)
    pine_gel_new_delivery = models.IntegerField(default=0)
    pine_gel_closing_stock = models.IntegerField(default=0)
    pine_gel_order_required = models.BooleanField(default=False)
    black_bags_new_delivery = models.IntegerField(default=0)
    black_bags_closing_stock = models.IntegerField(default=0)
    black_bags_order_required = models.BooleanField(default=False)
    hand_soap_new_delivery = models.IntegerField(default=0)
    hand_soap_closing_stock = models.IntegerField(default=0)
    hand_soap_order_required = models.BooleanField(default=False)
    apron_washing_powder_new_delivery = models.IntegerField(default=0)
    apron_washing_powder_closing_stock = models.IntegerField(default=0)
    apron_washing_powder_order_required = models.BooleanField(default=False)
    coke_zero_new_delivery = models.IntegerField(default=0)
    coke_zero_closing_stock = models.IntegerField(default=0)
    coke_zero_order_required = models.BooleanField(default=False)
    coke_new_delivery = models.IntegerField(default=0)
    coke_closing_stock = models.IntegerField(default=0)
    coke_order_required = models.BooleanField(default=False)
    fanta_new_delivery = models.IntegerField(default=0)
    fanta_closing_stock = models.IntegerField(default=0)
    fanta_order_required = models.BooleanField(default=False)
    iced_tea_peach_new_delivery = models.IntegerField(default=0)
    iced_tea_peach_closing_stock = models.IntegerField(default=0)
    iced_tea_peach_order_required = models.BooleanField(default=False)
    iced_tea_lemon_new_delivery = models.IntegerField(default=0)
    iced_tea_lemon_closing_stock = models.IntegerField(default=0)
    iced_tea_lemon_order_required = models.BooleanField(default=False)
    still_water_new_delivery = models.IntegerField(default=0)
    still_water_closing_stock = models.IntegerField(default=0)
    still_water_order_required = models.BooleanField(default=False)
    sparkling_water_new_delivery = models.IntegerField(default=0)
    sparkling_water_closing_stock = models.IntegerField(default=0)
    sparkling_water_order_required = models.BooleanField(default=False)
    sprite_new_delivery = models.IntegerField(default=0)
    sprite_closing_stock = models.IntegerField(default=0)
    sprite_order_required = models.BooleanField(default=False)
    heineken_zero_new_delivery = models.IntegerField(default=0)
    heineken_zero_closing_stock = models.IntegerField(default=0)
    heineken_zero_order_required = models.BooleanField(default=False)
    savanna_zero_new_delivery = models.IntegerField(default=0)
    savanna_zero_closing_stock = models.IntegerField(default=0)
    savanna_zero_order_required = models.BooleanField(default=False)
    flour_white_new_delivery = models.IntegerField(default=0)
    flour_white_closing_stock = models.IntegerField(default=0)
    flour_white_order_required = models.BooleanField(default=False)
    paper_towel_new_delivery = models.IntegerField(default=0)
    paper_towel_closing_stock = models.IntegerField(default=0)
    paper_towel_order_required = models.BooleanField(default=False)
    serviette_new_delivery = models.IntegerField(default=0)
    serviette_closing_stock = models.IntegerField(default=0)
    serviette_order_required = models.BooleanField(default=False)
    straws_new_delivery = models.IntegerField(default=0)
    straws_closing_stock = models.IntegerField(default=0)
    straws_order_required = models.BooleanField(default=False)
    foil_new_delivery = models.IntegerField(default=0)
    foil_closing_stock = models.IntegerField(default=0)
    foil_order_required = models.BooleanField(default=False)
    clingwrap_new_delivery = models.IntegerField(default=0)
    clingwrap_closing_stock = models.IntegerField(default=0)
    clingwrap_order_required = models.BooleanField(default=False)
    chilli_new_delivery = models.IntegerField(default=0)
    chilli_closing_stock = models.IntegerField(default=0)
    chilli_order_required = models.BooleanField(default=False)
    garlic_new_delivery = models.IntegerField(default=0)
    garlic_closing_stock = models.IntegerField(default=0)
    garlic_order_required = models.BooleanField(default=False)

from django.db import models

class DailyStock(models.Model):
    date = models.DateField()
    staff_name = models.CharField(max_length=100)
    
    # Define fields based on the provided form
    dough_balls_new_delivery = models.IntegerField(default=0)
    dough_balls_closing_stock = models.IntegerField(default=0)
    dough_balls_order_required = models.BooleanField(default=False)

    pizza_sauce_new_delivery = models.IntegerField(default=0)
    pizza_sauce_closing_stock = models.IntegerField(default=0)
    pizza_sauce_order_required = models.BooleanField(default=False)

    pizza_sauce_tin_new_delivery = models.IntegerField(default=0)
    pizza_sauce_tin_closing_stock = models.IntegerField(default=0)
    pizza_sauce_tin_order_required = models.BooleanField(default=False)

    pesto_sauce_new_delivery = models.IntegerField(default=0)
    pesto_sauce_closing_stock = models.IntegerField(default=0)
    pesto_sauce_order_required = models.BooleanField(default=False)

    fresh_mozzarella_new_delivery = models.IntegerField(default=0)
    fresh_mozzarella_closing_stock = models.IntegerField(default=0)
    fresh_mozzarella_order_required = models.BooleanField(default=False)

    ricotta_new_delivery = models.IntegerField(default=0)
    ricotta_closing_stock = models.IntegerField(default=0)
    ricotta_order_required = models.BooleanField(default=False)

    shredded_cheese_new_delivery = models.IntegerField(default=0)
    shredded_cheese_closing_stock = models.IntegerField(default=0)
    shredded_cheese_order_required = models.BooleanField(default=False)

    parmesan_new_delivery = models.IntegerField(default=0)
    parmesan_closing_stock = models.IntegerField(default=0)
    parmesan_order_required = models.BooleanField(default=False)

    blue_cheese_new_delivery = models.IntegerField(default=0)
    blue_cheese_closing_stock = models.IntegerField(default=0)
    blue_cheese_order_required = models.BooleanField(default=False)

    goat_cheese_new_delivery = models.IntegerField(default=0)
    goat_cheese_closing_stock = models.IntegerField(default=0)
    goat_cheese_order_required = models.BooleanField(default=False)

    feta_new_delivery = models.IntegerField(default=0)
    feta_closing_stock = models.IntegerField(default=0)
    feta_order_required = models.BooleanField(default=False)

    sundried_tomato_new_delivery = models.IntegerField(default=0)
    sundried_tomato_closing_stock = models.IntegerField(default=0)
    sundried_tomato_order_required = models.BooleanField(default=False)

    cooked_potato_new_delivery = models.IntegerField(default=0)
    cooked_potato_closing_stock = models.IntegerField(default=0)
    cooked_potato_order_required = models.BooleanField(default=False)

    raw_potato_new_delivery = models.IntegerField(default=0)
    raw_potato_closing_stock = models.IntegerField(default=0)
    raw_potato_order_required = models.BooleanField(default=False)

    zucchini_new_delivery = models.IntegerField(default=0)
    zucchini_closing_stock = models.IntegerField(default=0)
    zucchini_order_required = models.BooleanField(default=False)

    mushroom_new_delivery = models.IntegerField(default=0)
    mushroom_closing_stock = models.IntegerField(default=0)
    mushroom_order_required = models.BooleanField(default=False)

    caramelised_onion_new_delivery = models.IntegerField(default=0)
    caramelised_onion_closing_stock = models.IntegerField(default=0)
    caramelised_onion_order_required = models.BooleanField(default=False)

    sunflower_seeds_new_delivery = models.IntegerField(default=0)
    sunflower_seeds_closing_stock = models.IntegerField(default=0)
    sunflower_seeds_order_required = models.BooleanField(default=False)

    olives_new_delivery = models.IntegerField(default=0)
    olives_closing_stock = models.IntegerField(default=0)
    olives_order_required = models.BooleanField(default=False)

    spring_onion_new_delivery = models.IntegerField(default=0)
    spring_onion_closing_stock = models.IntegerField(default=0)
    spring_onion_order_required = models.BooleanField(default=False)

    peppadew_new_delivery = models.IntegerField(default=0)
    peppadew_closing_stock = models.IntegerField(default=0)
    peppadew_order_required = models.BooleanField(default=False)

    peppadew_tin_new_delivery = models.IntegerField(default=0)
    peppadew_tin_closing_stock = models.IntegerField(default=0)
    peppadew_tin_order_required = models.BooleanField(default=False)

    cooked_pineapple_new_delivery = models.IntegerField(default=0)
    cooked_pineapple_closing_stock = models.IntegerField(default=0)
    cooked_pineapple_order_required = models.BooleanField(default=False)

    pineapple_tin_new_delivery = models.IntegerField(default=0)
    pineapple_tin_closing_stock = models.IntegerField(default=0)
    pineapple_tin_order_required = models.BooleanField(default=False)

    artichoke_leaves_new_delivery = models.IntegerField(default=0)
    artichoke_leaves_closing_stock = models.IntegerField(default=0)
    artichoke_leaves_order_required = models.BooleanField(default=False)

    basil_new_delivery = models.IntegerField(default=0)
    basil_closing_stock = models.IntegerField(default=0)
    basil_order_required = models.BooleanField(default=False)

    rocket_new_delivery = models.IntegerField(default=0)
    rocket_closing_stock = models.IntegerField(default=0)
    rocket_order_required = models.BooleanField(default=False)

    coriander_new_delivery = models.IntegerField(default=0)
    coriander_closing_stock = models.IntegerField(default=0)
    coriander_order_required = models.BooleanField(default=False)

    pepperoni_new_delivery = models.IntegerField(default=0)
    pepperoni_closing_stock = models.IntegerField(default=0)
    pepperoni_order_required = models.BooleanField(default=False)

    parma_ham_new_delivery = models.IntegerField(default=0)
    parma_ham_closing_stock = models.IntegerField(default=0)
    parma_ham_order_required = models.BooleanField(default=False)

    cooked_bacon_new_delivery = models.IntegerField(default=0)
    cooked_bacon_closing_stock = models.IntegerField(default=0)
    cooked_bacon_order_required = models.BooleanField(default=False)

    rare_bacon_new_delivery = models.IntegerField(default=0)
    rare_bacon_closing_stock = models.IntegerField(default=0)
    rare_bacon_order_required = models.BooleanField(default=False)

    anchovies_new_delivery = models.IntegerField(default=0)
    anchovies_closing_stock = models.IntegerField(default=0)
    anchovies_order_required = models.BooleanField(default=False)

    chorizo_new_delivery = models.IntegerField(default=0)
    chorizo_closing_stock = models.IntegerField(default=0)
    chorizo_order_required = models.BooleanField(default=False)

    ham_new_delivery = models.IntegerField(default=0)
    ham_closing_stock = models.IntegerField(default=0)
    ham_order_required = models.BooleanField(default=False)

    cooked_chicken_new_delivery = models.IntegerField(default=0)
    cooked_chicken_closing_stock = models.IntegerField(default=0)
    cooked_chicken_order_required = models.BooleanField(default=False)

    raw_chicken_new_delivery = models.IntegerField(default=0)
    raw_chicken_closing_stock = models.IntegerField(default=0)
    raw_chicken_order_required = models.BooleanField(default=False)

    chilli_oil_new_delivery = models.IntegerField(default=0)
    chilli_oil_closing_stock = models.IntegerField(default=0)
    chilli_oil_order_required = models.BooleanField(default=False)

    truffle_oil_new_delivery = models.IntegerField(default=0)
    truffle_oil_closing_stock = models.IntegerField(default=0)
    truffle_oil_order_required = models.BooleanField(default=False)

    hummus_new_delivery = models.IntegerField(default=0)
    hummus_closing_stock = models.IntegerField(default=0)
    hummus_order_required = models.BooleanField(default=False)

    fig_jam_new_delivery = models.IntegerField(default=0)
    fig_jam_closing_stock = models.IntegerField(default=0)
    fig_jam_order_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Daily Stock on {self.date} by {self.staff_name}"


    def __str__(self):
        return f"{self.item_name} - {self.date}"
    

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

    def __str__(self):
        return f"{self.quantity_needed}g of {self.ingredient.name} for {self.pizza.name}"



