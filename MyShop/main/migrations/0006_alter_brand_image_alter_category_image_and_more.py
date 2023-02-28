# Generated by Django 4.1.5 on 2023-02-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_remove_product_price_productattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='media/brand_imgs/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/cat_imgs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/product_imgs/'),
        ),
    ]
