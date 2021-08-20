from django.db import models
from bg_store.models import CustomModel
from django.contrib.auth import get_user_model
from util.constants import GAME_GENRES, ACCESSORY
from django.forms import ModelForm
# Create your models here.

AuthUserModel = get_user_model()


class Publisher(CustomModel):
    name = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to='publisher image')
    details = models.CharField(max_length=250, null=True)
# how to add number of games in publisher brand

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Products(CustomModel):
    sku = models.CharField(
        max_length=50,
        null=True
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )
    description = models.TextField(
        null=True
    )
    image_cover = models.ImageField(
        upload_to='bg_cover'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00
    )
    player_count = models.CharField(
        max_length=10,
        null=False
    )
    new_stock = models.IntegerField(
        null=False,
        default=0
    )
    used_stock = models.IntegerField(
        null=False,
        default=0
    )
    difficulty = models.IntegerField(
        null=False,
        default=0
    )
    sales = models.IntegerField(
        null=False,
        default=0
    )
    bgg_link = models.CharField(
        max_length=250,
        null=False,
        default="https://boardgamegeek.com/"
    )
    image_game = models.ImageField(
        upload_to='product image'
    )
    category_name = models.CharField(
        max_length=40,
        null=False,
        unique=False,
        default="Product"
    )
    # purchase_price = models.DecimalField(
    #     max_digits=6,
    #     decimal_places=2,
    #     default=0.00
    # )
    genre = models.CharField(
        max_length=2,
        choices=GAME_GENRES,
        default=ACCESSORY
    )

    @property
    def image_url(self):
        return self.image_cover.url

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ProductForm(ModelForm):

    class Meta:
        model = Products
        fields = ['name', 'image_cover']


class Cart(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    data = models.JSONField(null=True)


