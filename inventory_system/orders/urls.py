# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Home page
    path('add/', views.add_order, name='add_order'),
    path('report/', views.daily_report, name='daily_report'),
    path('update-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('get-orders/', views.get_orders, name='get_orders'),
]



