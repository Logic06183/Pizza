from django.urls import path
from .views import weekly_stock_list, add_weekly_stock, ingredient_list, add_ingredient

urlpatterns = [
    path('stocks/', weekly_stock_list, name='weekly_stock_list'),
    path('stocks/add/', add_weekly_stock, name='add_weekly_stock'),
    path('ingredients/', ingredient_list, name='ingredient_list'),
    path('ingredients/add/', add_ingredient, name='add_ingredient'),
]


