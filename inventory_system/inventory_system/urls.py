# inventory_system/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import redirect_to_orders  # Import the redirect view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_orders),  # Redirect root URL to orders page
    path('orders/', include('orders.urls')),  # Include the orders app URLs
    path('stocks/', include('inventory.urls')),  # Include the inventory app URLs
]








