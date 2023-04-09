# Generated by Django 4.1.5 on 2023-04-09 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='ID пользователя')),
                ('id_product', models.IntegerField(verbose_name='ID товара')),
                ('count', models.IntegerField(verbose_name='Количество товара')),
            ],
            options={
                'verbose_name': 'Корзины',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='ID пользователя')),
                ('id_product', models.IntegerField(verbose_name='ID товара')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('brand', models.CharField(max_length=50, verbose_name='Название бренда производителя')),
                ('category', models.CharField(max_length=40, verbose_name='Категория')),
                ('img_file', models.FileField(upload_to='', verbose_name='Файл')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('discount', models.BooleanField(default=False, verbose_name='Есть ли скидка на товар')),
                ('price_with_discount', models.IntegerField(verbose_name='Цена со скидкой')),
                ('percent_discount', models.IntegerField(default=0, verbose_name='Процент скидки')),
                ('count', models.IntegerField(default=1, verbose_name='Количество товара (в шк)')),
                ('seller', models.CharField(default='Red Catalog', max_length=40, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='ID пользователя')),
                ('id_product', models.IntegerField(verbose_name='ID товара')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата и время покупки')),
            ],
            options={
                'verbose_name': 'Купленное',
                'verbose_name_plural': 'Купленное',
            },
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='ID пользователя')),
                ('id_product', models.IntegerField(verbose_name='ID товара')),
            ],
            options={
                'verbose_name': 'Проданное',
                'verbose_name_plural': 'Проданное',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Электронная почта')),
                ('password', models.CharField(max_length=35, verbose_name='Пароль')),
                ('user_name', models.CharField(blank=True, default='', max_length=25, verbose_name='Имя')),
                ('user_surname', models.CharField(blank=True, default='', max_length=25, verbose_name='Фамилия')),
                ('img_file', models.FileField(upload_to='', verbose_name='Файл аватарки')),
                ('age', models.CharField(blank=True, default='', max_length=25, verbose_name='Возраст')),
                ('city', models.CharField(blank=True, default='', max_length=40, verbose_name='Город')),
                ('money', models.IntegerField(default=100000, verbose_name='Баланс')),
                ('products_purchased', models.IntegerField(default=0, verbose_name='Количество купленных товаров')),
                ('products_sold', models.IntegerField(default=0, verbose_name='Колчество проданных товаров')),
                ('money_earned', models.IntegerField(default=0, verbose_name='Заработок на продажах')),
                ('money_spend', models.IntegerField(default=0, verbose_name='Потрачено на покупки')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
