# Generated by Django 4.1.5 on 2023-02-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_isfeatured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='isFeatured',
            new_name='isfeatured',
        ),
    ]
