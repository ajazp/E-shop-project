# Generated by Django 4.0 on 2022-06-21 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0002_rename_uname_userreg_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreg',
            old_name='email',
            new_name='comfirm_password',
        ),
        migrations.RenameField(
            model_name='userreg',
            old_name='repassword',
            new_name='your_email',
        ),
    ]
