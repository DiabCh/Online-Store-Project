from products_stock.models import Products, Publisher
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse, Http404
from util.cart import Cart
from products_stock.forms.filter import SearchAndFilter
from django.shortcuts import render


def StoreList(request):

    form = SearchAndFilter(request.GET)
    product_list = form.get_filtered_products()
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    # page_num = page_obj.num_pages
    page_num = paginator.num_pages

    return render(request, 'products/list.html', {

        'page_obj': page_obj,
        'form': form,
        'page_num': page_num,

    })


def publisher_list(request):

    publishers = Publisher.objects.all().order_by('name')

    return render(request, 'publishers/publisher_list.html',{
        'publishers': publishers
    })


def publisher_page(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    publisher_products = Products.objects.filter(publisher=publisher_id)

    return render(request, 'publishers/publisher_page.html',
                  {
                      'publisher': publisher,
                      'publisher_products': publisher_products,
                  })


def product_page(request, product_id):
    # print('\n\n\n\nproduct_page\n')
    # print(request.GET)
    # product = Products.objects.filter(pk=product_id).all()
    product = Products.objects.get(pk=product_id)
    return render(request, 'products/product_page.html', {
        'product': product
    })
    # return render(request, 'products/product_page.html')


def add_to_cart(request, product_id):
    page = request.POST.get('page', 1)

    # next_url = request.GET.get('next') # not required
    # when using POST, you have to redirect

    # Post contains the quantity
    try:
        quantity = int(request.POST['quantity'])
    except ValueError as e:
        raise Http404(e)

    cart = Cart(request.user, request.session)
    cart.update(product_id, quantity)

    return redirect('%s?page=%s' % (
        reverse('products:store_list'),
        page
        ))


