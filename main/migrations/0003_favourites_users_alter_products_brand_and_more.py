# Generated by Django 4.1.7 on 2023-03-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_options_products_img_link'),
    ]

    operations = [
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
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Электронная почта')),
                ('password', models.CharField(max_length=35, verbose_name='Пароль')),
                ('user_name', models.CharField(default='', max_length=25, verbose_name='Имя')),
                ('user_surname', models.CharField(default='', max_length=25, verbose_name='Фамилия')),
                ('age', models.IntegerField(default=18, verbose_name='Возраст')),
                ('sity', models.CharField(default='', max_length=40, verbose_name='Город')),
                ('money', models.IntegerField(default=100000, verbose_name='Баланс')),
                ('flag', models.BooleanField(default=False, verbose_name='Продавец или нет')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Название бренда производителя'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_with_discount',
            field=models.IntegerField(verbose_name='Цена со скидкой'),
        ),
    ]
