# Generated by Django 4.1.5 on 2023-01-17 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_alter_order_product_quantity'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='carts',
        ),
    ]