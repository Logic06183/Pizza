from django.utils import timezone

class Order:
    def __init__(self):
        self.pizzas = []
        self.status = 'pending'
        self.created_at = timezone.now()
        self.due_time = timezone.now() + timezone.timedelta(minutes=30)

    def add_pizza(self, pizza_name, quantity=1, special_instructions=''):
        self.pizzas.append({
            'pizza_name': pizza_name,
            'quantity': quantity,
            'special_instructions': special_instructions
        })

    def submit_order(self):
        from orders.models import Order as OrderModel, OrderItem
        # Create order in database
        order = OrderModel.objects.create(
            status=self.status,
            created_at=self.created_at,
            due_time=self.due_time
        )
        # Create order items
        for pizza in self.pizzas:
            OrderItem.objects.create(
                order=order,
                pizza_name=pizza['pizza_name'],
                quantity=pizza['quantity'],
                special_instructions=pizza['special_instructions']
            )
        return order