# Generated by Django 3.1.7 on 2021-06-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_stock', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='genre',
            field=models.CharField(choices=[('AC', 'Accessory'), ('FG', 'Family Game'), ('DG', 'Dexterity Game'), ('PG', 'Party Game'), ('A', 'Abstract Game'), ('TG', 'Thematic Game'), ('EG', 'Eurogame'), ('WG', 'Wargame'), ('AR', 'Area Control'), ('L', 'Legacy'), ('DB', 'Deckbuilder'), ('DR', 'Drafting'), ('DC', 'Dungeon Crawler'), ('WP', 'Worker Placement'), ('MI', 'Miniature')], default='AC', max_length=2),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_cover',
            field=models.ImageField(upload_to='bg_cover'),
        ),
    ]
