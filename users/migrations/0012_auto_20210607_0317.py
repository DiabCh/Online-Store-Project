# Generated by Django 3.1.7 on 2021-06-07 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210606_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 3, 47, 37, 718539)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='29d8d0d99ab4aee24bb82342696bfdf33b4a5ecc4c2c65fa0d117fd7f25bf7a6', max_length=64),
        ),
    ]
