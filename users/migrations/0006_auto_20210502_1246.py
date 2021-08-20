# Generated by Django 3.1.7 on 2021-05-02 09:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210502_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 10, 16, 22, 389981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='d26e44ba5544248225851e21dbcf822913d08e406d54cb3b1b76f914370bfd67', max_length=64),
        ),
    ]
