# Generated by Django 3.1.7 on 2021-06-09 03:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210608_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 9, 4, 19, 14, 564398)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='15a4487b0888c3b236bfd0108529656e1f27017ef6bdb2175ee2cca325cc442c', max_length=64),
        ),
    ]
