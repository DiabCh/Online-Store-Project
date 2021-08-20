from django import forms
from products_stock.models import Products
from util.constants import GAME_GENRES
from django.db import models
from products_stock.models import Products


class OrderBy(models.TextChoices):
    LATEST = 'latest_products', 'Latest'
    POPULARITY = 'popularity', 'Popularity'
    PRICE_ASC = 'price_asc', 'Price Ascending'
    PRICE_DESC = 'price_desc', 'Price descending'


class SearchAndFilter(forms.Form):
    search_term = forms.CharField(max_length=255, required=False, label='Search')
    order_by = forms.ChoiceField(choices=OrderBy.choices, required=False)
    genres = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=False,
        label="Game Genre's",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        products = Products.objects.all()
        products_choice = tuple(
            [(product.id, product.genre) for product in products]
        )
        # print('PRODUCT CHOICE', products_choice)
        self.fields['genres'].choices = GAME_GENRES
        # print('game_genres', GAME_GENRES)

    # def clean_products(self):
    #     print('this works')
    #     products = self.cleaned_data.get('products', [])
    #     print(products)
    #
    #     return products

    def get_filtered_products(self):
        # with is_valid Django creates the `cleaned_data` dictionary with all the cleaned informations.
        if self.is_valid():
            search_term = self.cleaned_data.get('search_term', None)
            order_by = self.cleaned_data.get('order_by', OrderBy.POPULARITY)
            genres = self.cleaned_data.get('genres', [])

            product_list = Products.objects.order_by('-created_at')

            if search_term:
                product_list = product_list.filter(name__icontains=search_term)

            if order_by == OrderBy.PRICE_ASC:
                product_list = product_list.order_by('price')
            elif order_by == OrderBy.PRICE_DESC:
                product_list = product_list.order_by('-price')
            elif order_by == OrderBy.LATEST:
                product_list = product_list.order_by('-created_at')
            elif order_by == OrderBy.POPULARITY:
                product_list = product_list.order_by('-sales')

            if genres:
                product_list = product_list.filter(
                    genre__in=genres)

            return product_list

        return Products.objects.all()