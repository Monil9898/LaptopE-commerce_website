# Generated by Django 4.1.6 on 2023-03-08 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0021_alter_cart_product_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesories_pro',
            name='accesories_accesories_idaccesories',
        ),
        migrations.RemoveField(
            model_name='accesories_pro',
            name='offer_offer_idOffer',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='accessories_qty',
        ),
        migrations.DeleteModel(
            name='Accesories',
        ),
        migrations.DeleteModel(
            name='Accesories_Pro',
        ),
    ]
