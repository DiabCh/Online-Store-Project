from django.core.management import BaseCommand, CommandError
import os
import json
from products_stock.models import Products, Publisher



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file')
        if not file_path:
            raise CommandError("file not provided")
        if not file_path.endswith('.xlxs'):
            raise CommandError("import supports only .xlxs files")
        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                products = json.load(import_file)

        except FileNotFoundError as e:
            raise CommandError('file at %s was not found:' % os.path.join('data', file_path))
        for product in products:
            publisher_id = Publisher.objects.get(pk=product['publisher'])

            db_products = Products(

                publisher=Publisher.objects.get(pk=product['publisher']),
                # look at ingeriendts for assignment value
                name=product['name'],
                description=product['description'],
                image_cover=product['image_cover'],
                price=product['price'],
                genre=product['genre'],
                player_count=product['player_count'],
                new_stock=product['new_stock'],
                used_stock=product['used_stock'],
                difficulty=product['difficulty'],
                sales=product['sales'],
                bgg_link=product['bgg_link'],
                image_game=product['image_game'],
                category_name=product['category_name']
            )
            db_products.save()
