from products_stock.models import Cart as CartModel
import json


class Cart:
    def __init__(self, user, session):
        self._user = user
        self._session = session
        self._data = session.get('cart', {})

    def update(self, product_id, quantity):
        product_id_key = str(product_id)

        if quantity == 0:
            if product_id_key in self._data:
                del self._data[product_id_key]
        else:
            self._data[product_id_key] = quantity

        self._save()

    def _save(self):
        try:
            cart_model = CartModel.objects.get(user=self._user)
            cart_model.data = json.dumps(self._data)
        except CartModel.DoesNotExist:
            cart_model = CartModel(user=self._user, data=json.dumps(self._data))

        cart_model.save()
        self._session['cart'] = self._data

    def delete(self):
        del self._session['cart']
        CartModel.objects.get(user=self._user).delete()


    @staticmethod
    def load(user, session):
        try:
            cart_model = CartModel.objects.get(user=user)
            cart_data = json.loads(cart_model.data)
        except CartModel.DoesNotExist:
            cart_data = {}

        session['cart'] = cart_data