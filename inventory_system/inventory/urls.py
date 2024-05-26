from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.weekly_stock_list, name='weekly_stock_list'),
    path('stocks/add/', views.add_weekly_stock, name='add_weekly_stock'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/add/', views.add_ingredient, name='add_ingredient'),
    path('daily_stocks/', views.daily_stock_list, name='daily_stock_list'),
    path('daily_stocks/add/', views.add_daily_stock, name='add_daily_stock'),
]




