# Generated by Django 4.2.5 on 2023-09-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0008_brand_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ManyToManyField(to='products_app.brand'),
        ),
    ]