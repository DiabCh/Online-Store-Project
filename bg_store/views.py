from django.shortcuts import render
from products_stock.models import Products
from itertools import islice
import datetime
from datetime import date


def homepage_view(request):
    # if request.user.is_authenticated:
    #     print('user', request.user)
    #     print('credits', request.user.profile.credit)
    products_new = Products.objects.all().order_by('-id')

    products_best_sellers = Products.objects.exclude(
        created_at__lt=
        date.today() - datetime.timedelta(weeks=4)).order_by('-sales')

    new_products = islice(products_new, 5)
    best_sellers = islice(products_best_sellers, 5)
    # for x in range(5):
    #     new_products.append(products_new[x])
    #     best_sellers.append(products_best_sellers[x])
    return render(request, "homepage.html", {
        "brand": "Diab's boardgame emporium",
        "new_products": new_products,
        "best_sellers": best_sellers
    })


def contact_view(request):
    return render(request, "contact.html")


def sell_view(request):
    return render(request, "sell_boardgame.html")


def about_us_view(request):
    return render(request, 'about_us.html')


def payment_and_delivery(request):
    return render(request, 'payment_delivery.html')
