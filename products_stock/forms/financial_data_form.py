from django import forms
import datetime
from orders.models import OrderItem


def get_item_quantity(min_date, max_date):
    pass


class FinancialForm(forms.Form):

    min_date_range = forms.DateField(label='Starting date',
                                     widget=forms.SelectDateWidget)
    max_date_range = forms.DateField(label='Ending date',
                                     widget=forms.SelectDateWidget)

    def retrieve_order_items_date_range(self):

        min_date_range = self.cleaned_data.get('min_date_range')
        max_date_range = self.cleaned_data.get('max_date_range') + datetime.timedelta(days=1)
        order_items_last_month = OrderItem.objects.filter(
            created_at__gte=min_date_range,
            created_at__lte=max_date_range)

        order_item_dict = {}

        for order_item in order_items_last_month:
            if order_item.item_id in order_item_dict:
                order_item_dict[order_item.item_id] += order_item.quantity
            else:
                order_item_dict[order_item.item_id] = order_item.quantity

        return order_item_dict

