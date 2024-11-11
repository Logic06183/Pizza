
def add_order():
    order = Order()
    while True:
        pizza_name = input("Enter pizza name (or 'done' to finish): ")
        if pizza_name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        special_instructions = input("Enter special instructions (if any): ")
        order.add_pizza(pizza_name, quantity, special_instructions)