import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, Http404
from django.contrib.auth.decorators import login_required
from products_stock.models import Products
from django.contrib.sites.models import Site
from urllib.parse import urlencode



@login_required
def order_view(request):

    cards = stripe.Customer.list_sources(
        request.user.stripe_customer.stripe_id,
        object='card',
        api_key=settings.STRIPE_SECRET_KEY,
    )

    return render(request, 'orders/orders.html', {
        'cards': cards
    })


@login_required
def pay_order(request):

    payment_method = request.POST['card_id']
    if request.method != 'POST' and payment_method:
        raise Http404('Method not allowed')

    site_domain = Site.objects.get_current().domain

    # calculates final price.
    cart_data = request.session['cart']
    product_list = Products.objects.filter(id__in=cart_data.keys())
    total_price = sum([product.price * cart_data[str(product.id)] for product in product_list])

    payment_intent = stripe.PaymentIntent.create(
        amount=int(total_price) * 100,
        currency='RON',
        confirm=True,
        return_url='%s%s' % (site_domain, reverse('payments:3d_secure')),
        customer=request.user.stripe_customer.stripe_id,
        payment_method=payment_method,
        api_key=settings.STRIPE_SECRET_KEY,
    )

    card_id = payment_intent.stripe_id

    # if 3d secure
    next_action = payment_intent['next_action']
    if next_action:
        return redirect(next_action['redirect_to_url']['url'])

    # if not 3d secure

    return redirect(reverse('payments:process', args=(card_id,)))




