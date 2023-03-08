# Generated by Django 4.1.7 on 2023-03-08 10:56

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
                ('product_name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('brand', models.CharField(max_length=30, verbose_name='Название бренда производителя')),
                ('category', models.CharField(max_length=40, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('discount', models.BooleanField(default=False, verbose_name='Есть ли скидка на товар')),
                ('price_with_discount', models.IntegerField(default=models.IntegerField(verbose_name='Цена'), verbose_name='Цена со скидкой')),
                ('percent_discount', models.IntegerField(default=0, verbose_name='Процент скидки')),
            ],
        ),
    ]
