from django.shortcuts import render, redirect, reverse, get_object_or_404, Http404
from users.forms import RegisterForm, AddressForm
from django.contrib.auth.decorators import login_required
from users.models.user_data import Notification
from orders.models import Order, OrderItem
from products_stock.models import Products
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from users.models import Address


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()

    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # send_register_email(user)
            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form
    })


@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user, seen=False).all()

    return render(request, 'users/notifications.html', {
        'notifications': notifications
    })


@login_required
def mark_notification_as_seen(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.seen = True
    notification.save()
    return redirect(reverse('users:account:notifications'))


@login_required
def profile_view(request):
    return render(request, 'users/my_profile.html')


@login_required
def order_history_view(request):
    user_orders_list = [order for order in
                        Order.objects.filter(user_id=request.user.id)]
    # print('user id ', request.user.id)
    # print('USER ORDER LIST', user_orders_list)
    order_item_list =[OrderItem.objects.filter(order_id=order) for order in user_orders_list]
    # print('ORDER ITEM LIST ',order_item_list)
    total_price_list = []
    for item in order_item_list:
        total_price = 0
        for x in item:
            total_price += Products.objects.get(id=x.item_id).price * OrderItem.objects.get(id=x.id).quantity

        total_price_list.append(int(total_price))

    to_send = zip(user_orders_list, total_price_list)
    return render(request, 'users/order_history.html', {
        'list': to_send,

    })


@login_required
def order_details_view(request, order_id):
    products = Products.objects.filter(
        orders__id=order_id
    )
    print(products)
    quantities = [x.quantity for x in OrderItem.objects.filter(order_id=order_id)]

    list = zip(products, quantities)
    return render(request, 'users/order_details.html', {
        'list': list,
        'order_id': order_id
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users/change_password.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def view_addresses(request):
    print(request.user)
    user_addresses = Address.objects.filter(user_id=request.user)
    return render(request, 'users/view_addresses.html',{
        'user_addresses': user_addresses
    })


@login_required
def add_address(request):
    # when submit is pressed
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.clean_address_data(request.user)
            return redirect(reverse('users:account:address_view'))
    else:
        form = AddressForm()

    return render(request, 'users/add_address.html', {
        'form': form,
    })


@login_required
def remove_address(request, address_id):
    address = Address.objects.filter(id=address_id)
    address.delete()
    return redirect(reverse('users:account:address_view'))