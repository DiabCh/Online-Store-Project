from django.shortcuts import render
from products_stock.models import Products
from django.contrib.auth.decorators import login_required


@login_required
def view(request):
    cart = request.session.get('cart', {})
    product_list = Products.objects.filter(id__in=cart.keys())
    return render(request, 'cart/view_cart.html', {
        'product_list': product_list

    })