# Generated by Django 4.1.5 on 2023-01-20 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0028_address_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='order',
            new_name='orders',
        ),
    ]