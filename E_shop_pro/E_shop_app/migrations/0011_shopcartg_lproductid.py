# Generated by Django 4.0 on 2022-07-01 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0010_remove_shopcart_gproductid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcartg',
            name='Lproductid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='E_shop_app.lpro_db'),
        ),
    ]