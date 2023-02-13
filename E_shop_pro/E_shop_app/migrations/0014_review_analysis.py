# Generated by Django 4.0.6 on 2022-11-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0013_shopcheckout_address1_shopcheckout_address2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothingid', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('reviewtext', models.TextField(max_length=200, null=True)),
                ('rating', models.IntegerField(null=True)),
                ('Recommended', models.IntegerField(null=True)),
                ('Positive', models.CharField(max_length=200, null=True)),
                ('Division_Name', models.CharField(max_length=200, null=True)),
                ('Department_Name', models.ImageField(null=True, upload_to='image')),
            ],
        ),
    ]