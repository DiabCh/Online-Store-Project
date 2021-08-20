from django.urls import path
from products_stock.views.cart import view

app_name = 'cart'

urlpatterns = [
    path('', view, name='view')
]