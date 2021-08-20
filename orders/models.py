from django.db import models
from django.core.validators import MinValueValidator
from bg_store.models import CustomModel
from django.contrib.auth import get_user_model
from products_stock.models import Products

AuthUserModel = get_user_model()


class Order(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products, through='OrderItem', #Products.orders
                                   related_name='orders'
                                   )


class OrderItem(CustomModel):
    item = models.ForeignKey(Products, on_delete=models.CASCADE,    #Products.order_items
                             related_name='order_items'
                             )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, #Order.order_items
                              related_name='order_items'
                              )
    quantity = models.IntegerField(default=1,
                                   validators=[MinValueValidator(1)]
                                   )
