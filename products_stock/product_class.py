from dataclasses import dataclass
from products_stock.models import Products, Publisher


class ProductClass:
    def __init__(self, product_data): # remove init, add the dataclasses
        # name: str
        # description: str
        # price: int
        # genre: str
        # player_count: int
        # stock: int
        # used_stock: int
        # difficulty: int
        # publisher: int
        # bgg_link: str
        # category: str
        # recent_sales: int
        # product_image: str
        # sku: product_data['name'][0:2] + product_data['name'][-1]
        self.sku = str((product_data[1][0:2] + product_data[1][-3:-1]) + '-' + str(product_data[3]))
        self.name = product_data[1]
        self.description = product_data[2]
        self.price = product_data[3]
        self.genre = product_data[4]
        self.player_count = product_data[5]
        self.stock = product_data[6]
        self.used_stock = product_data[7]
        self.difficulty = product_data[8]
        self.publisher = product_data[9]
        self.bgg_link = product_data[10]
        self.category = product_data[11]
        self.recent_sales = product_data[12]
        self.product_image = product_data[13]


    def verify_prod(self):

        self.check_duplicate()

    def verify_data(self):
        pass

    def check_duplicate(self):
        if Products.objects.filter(name__icontains=self.name):
            print('Already exists')

        else:
            print('Not in')
            self.save_to_db()

    def save_to_db(self):
        db_products = Products(

            publisher=Publisher.objects.get(pk=self.publisher),
            name=self.name,
            description=self.description,
            image_cover=self.product_image,
            price=self.price,
            genre=self.genre,
            player_count=self.player_count,
            new_stock=self.stock,
            used_stock=self.used_stock,
            difficulty=self.difficulty,
            sales=0,
            bgg_link=self.bgg_link,
            image_game=self.product_image,
            category_name=self.category,
            sku=self.sku
        )
        db_products.save()

    def update_sales(self):
        pass

    def upload_product_image(self):
        pass
