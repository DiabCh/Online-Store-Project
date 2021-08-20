from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile, Activation
from users.models.user_data import Notification
from users.emails import send_activation_mail
from django.contrib.auth.signals import user_logged_in
from util.cart import Cart
from products_stock.models import Publisher, Products
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from util.constants import ACTIVATION_AVAILABILITY_DICT

AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    # if not instance.pk checks if an user exists in the database
    # by checking if a pk exists
    if not instance.pk and not hasattr(instance, "is_social_auth"):
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    # print('*' * 100)
    # print('instance', instance)
    # print('created', created)
    # print('kwargs', kwargs)
    if created:
        Profile(user=instance).save()


@receiver(post_save, sender=AuthUserModel)
def set_activation_details(instance, created, **kwargs):
    if created and not instance.is_active:
        activation = Activation(user=instance)
        activation.save()
        print(timezone.now() + timezone.timedelta(
            **ACTIVATION_AVAILABILITY_DICT))
        send_activation_mail(activation)


@receiver(user_logged_in)
def get_cart_data(request, user, **kwargs):
    Cart.load(user, request.session)


@receiver(post_save, sender=Products)
def product_notification(instance, created, **kwargs):
    if created:
        # users = AuthUserModel.objects.exclude(is_staff=True).all()
        users = AuthUserModel.objects.filter(is_staff=False).all()
        for user in users:
            notification = Notification(
                user=user,
                content_object=instance,
                message='A new product has been added to our catalogue!',
                link=reverse('products:product_page:details', args=(instance.id,)),

            )
            notification.save()


@receiver(pre_save, sender=Products)
def product_discount_notification(instance, **kwargs):

    if instance.pk: # object already existed before the update was done
        current_price = Products.objects.get(pk=instance.pk).price

        if instance.price < current_price:
            users = AuthUserModel.objects.filter(is_staff=False).all()
            for user in users:
                notification = Notification(
                    user=user,
                    content_object=instance,
                    message='A discount has been applied to this product',
                    link=reverse('products:product_page:details',
                                 args=(instance.id,)),

                )
                notification.save()
