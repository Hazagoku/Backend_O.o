# Generated by Django 3.1.7 on 2021-03-05 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_compra_favorite_user_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='car_id',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='car_id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]