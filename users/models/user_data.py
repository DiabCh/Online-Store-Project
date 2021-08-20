from django.db import models
from django.contrib.auth import get_user_model
from bg_store.models import CustomModel
from util.constants import SHIPPING_ADDRESS, BILLING_ADDRESS
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import  ContentType


# Create your models here.
AuthUserModel = get_user_model()


class Address(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    country = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    sector = models.IntegerField(null=False)
    street = models.CharField(max_length=255, null=False)
    building = models.CharField(max_length=255, null=False)
    floor = models.CharField(max_length=255, null=False)
    appartment = models.CharField(max_length=10, null=False)

    class Types(models.IntegerChoices):
        SHIPPING = SHIPPING_ADDRESS
        BILLING = BILLING_ADDRESS
    type = models.IntegerField(choices=Types.choices, null=False, default=1)


class Profile(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile', null=False,default="nerd")
    avatar = models.ImageField(upload_to='profiles', default=None, null=True)
    credit = models.IntegerField(null=False, default=0)
    membership = models.BooleanField(null=False, default=False)
    collection = models.ImageField(upload_to='profiles', default="profiles/cobweb.jpg", null=False)

    
class Notification(CustomModel):
    # user that receives a notification
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    message = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)