from products_stock.models import Products
import stripe
from django.shortcuts import Http404, redirect, reverse
from django.conf import settings
from orders.models import Order, OrderItem
from django.contrib.auth import get_user_model
from util.cart import Cart
AuthUserModel = get_user_model()


def process_payment_helper(request, payment_intent_id):
    if not payment_intent_id:
        raise Http404('Method not allowed.')

    # retrieves payment intent
    payment_intent = stripe.PaymentIntent.retrieve(
        payment_intent_id,
        api_key=settings.STRIPE_SECRET_KEY
    )
    # checks for payment error
    if payment_intent['last_payment_error']:
        return redirect(reverse('payments:failed'))

    # payment successful

    # creates order obj in database
    order_obj = Order(user=request.user)
    order_obj.save()

    cart = request.session['cart']

    for product, quantity in cart.items():
        product_object = Products.objects.get(id=product)
        # updates sales for products

        new_sale_value = int(product_object.sales) + int(quantity)
        Products.objects.filter(pk=product).update(sales=new_sale_value)

        # saving every item as a separate order item
        order_item_object = OrderItem(
            item=product_object,
            order=order_obj,
            quantity=quantity
        )
        order_item_object.save()

    # delete cart

    Cart(user=request.user, session=request.session).delete()

    return redirect('/')
