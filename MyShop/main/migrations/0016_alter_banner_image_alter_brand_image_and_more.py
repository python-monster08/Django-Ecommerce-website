# Generated by Django 4.1.5 on 2023-02-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_img_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner_images/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brand_imgs/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='cat_imgs/'),
        ),
    ]
