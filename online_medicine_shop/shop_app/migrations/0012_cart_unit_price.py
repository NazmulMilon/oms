# Generated by Django 4.1.5 on 2023-01-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0011_rename_product_quantity_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='product_unit_price', max_digits=10),
            preserve_default=False,
        ),
    ]
