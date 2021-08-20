from django.urls import path, include
from products_stock.views.product_page import StoreList
from products_stock.views.product_page import add_to_cart
app_name = 'products'

urlpatterns = [
    path('', StoreList, name='store_list'),
    path('info/', include('products_stock.urls.product_page')),
    path('cart/', include('products_stock.urls.cart')),
    path('publisher/',  include('products_stock.urls.publisher')),
    path('<int:product_id>/add_to_cart/', add_to_cart, name='add_to_cart'),



]
# path('', StoreList.as_view())
