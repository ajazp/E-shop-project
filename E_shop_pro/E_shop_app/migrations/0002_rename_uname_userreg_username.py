# Generated by Django 4.0 on 2022-06-21 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreg',
            old_name='uname',
            new_name='username',
        ),
    ]