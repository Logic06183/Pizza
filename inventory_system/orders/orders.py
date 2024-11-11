
class Order:
    def __init__(self):
        self.pizzas = []  # List to store pizzas in the order

    def add_pizza(self, pizza_name, quantity=1, special_instructions=''):
        self.pizzas.append({
            'pizza_name': pizza_name,
            'quantity': quantity,
            'special_instructions': special_instructions
        })