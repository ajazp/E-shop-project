# Generated by Django 3.2 on 2022-12-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0014_review_analysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.TextField(max_length=500, null=True)),
                ('re', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
