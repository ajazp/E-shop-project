# Generated by Django 4.0 on 2022-06-22 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0005_rename_description_brandladies_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='bimg',
            new_name='img',
        ),
    ]
