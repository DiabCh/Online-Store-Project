from django.core.management import BaseCommand, CommandError
import os
import json
from django.contrib.auth import get_user_model
from products_stock.models import Publisher

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file')
        if not file_path:
            raise CommandError("file not provided")
        if not file_path.endswith('.json'):
            raise CommandError("import supports only .json files")
        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                publisher = json.load(import_file)

        except FileNotFoundError as e:
            raise CommandError('file at %s was not found:' % os.path.join('data', file_path))

        for item in publisher:
            db_publisher = Publisher(
                name=item['name'],
                image=item['image'],
                details=item['details']
            )
            db_publisher.save()
