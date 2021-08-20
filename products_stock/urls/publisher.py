from django.urls import path
from products_stock.views.product_page import publisher_list, publisher_page


app_name = 'publisher'

urlpatterns = [
    path('publisher_list/', publisher_list, name='publisher_list'),
    path('<int:publisher_id>/', publisher_page, name='publisher_details'),
]
