# Generated by Django 3.2 on 2021-04-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20, verbose_name='Product Name')),
                ('product_quantity', models.IntegerField(verbose_name='Product Quantity')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Price')),
            ],
        ),
    ]
