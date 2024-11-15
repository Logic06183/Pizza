
def order_list(request):
    # ...existing code...
    context = {
        # ...existing context variables...
        'featured_pizza_numbers': [1, 2, 3],
    }
    return render(request, 'orders/order_list.html', context)