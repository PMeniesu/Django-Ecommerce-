# Generated by Django 5.1.3 on 2024-11-26 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_categories_category_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=datetime.datetime(2024, 11, 26, 17, 26, 57, 557459), max_digits=6),
        ),
    ]