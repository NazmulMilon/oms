# Generated by Django 4.1.5 on 2023-01-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0025_alter_address_address_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[(1, 'SHIPPING_ADDRESS'), (2, 'BILLING_ADDRESS')], default=1, max_length=50),
        ),
    ]
