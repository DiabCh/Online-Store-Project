from django import template
from products_stock.models import Products
register = template.Library()


@register.filter(name='products_or_price')
def cart_product_count(cart_dicts, type_=None):
    if type_ == 'price':
        product_list = Products.objects.filter(id__in=cart_dicts.keys())
        cart_sum = [int(product.price) for product in product_list]

        return sum([product.price * cart_dicts[str(product.id)] for product in product_list])

    return sum([int(cart_value) for cart_value in cart_dicts.values()])


@register.simple_tag(name='cart_data', takes_context=True)
def get_cart_data(context, *args, **kwargs):

    cart_dict = context.request.session.get('cart', {})
    # print(cart_dict)
    product_list = Products.objects.filter(id__in=cart_dict.keys())
    product_number = sum([int(cart_value) for cart_value in cart_dict.values()])

    total_price = '%.2f RON' % sum([product.price * cart_dict[str(product.id)] for product in product_list])

    return {
        'products': product_number,
        'price': total_price
    }


@register.filter(name='visible_pages')
def visible_pages(page_obj): # page_obj contains the current page data
    # print('******','page obj', '*********')
    # print(page_obj)
    paginator = page_obj.paginator
    # generates a paginator object
    pages = list(page_obj.paginator)
    current_page = page_obj.number
    first_pages = pages[0:2]
    last_pages = pages[-2:]

    if len(paginator.page_range) <= 4:
        return pages

    if current_page == 1 or current_page == paginator.num_pages:
        return first_pages + [None] + last_pages

    current_page_index = [page.number for page in pages].index(current_page)

    if current_page >= len(paginator.page_range) - 2:
        return first_pages + [None] + pages[
                                      current_page_index - 1:current_page_index + 2]
    if current_page <= 3:
        return pages[current_page_index-1:current_page_index + 2] + [None] + last_pages

    return first_pages + [None] + pages[current_page_index-1:current_page_index + 2] + [None] + last_pages


@register.filter(name='product_value')
def get_product_value_from_cart(session, product_id):

    # print('**************', 'product_id')
    # print(product_id)
    if 'cart' in session:
        # print('***************', 'session')

        return session['cart'].get(str(product_id), 0)

    return 0
