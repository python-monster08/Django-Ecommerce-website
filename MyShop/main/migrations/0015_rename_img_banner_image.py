# Generated by Django 4.1.5 on 2023-02-25 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_banner_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='img',
            new_name='image',
        ),
    ]
