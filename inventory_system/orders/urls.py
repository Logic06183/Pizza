# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('', views.order_list, name='order_list'),
    path('report/', views.daily_report, name='daily_report'),  # Ensure this is included
]



