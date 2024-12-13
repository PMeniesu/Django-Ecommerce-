# Generated by Django 5.1.3 on 2024-11-26 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=datetime.datetime(2024, 11, 26, 17, 21, 38, 206748), max_digits=6),
        ),
    ]
