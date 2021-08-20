from django.urls import path
from products_stock.views.product_page import product_page

# products:product_page
app_name = 'product_page'

urlpatterns = [
    path('<int:product_id>/', product_page, name='details'),

]
