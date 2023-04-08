# Generated by Django 4.1.5 on 2023-03-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_users_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='users',
            name='sity',
        ),
        migrations.AddField(
            model_name='users',
            name='city',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='users',
            name='img_link',
            field=models.TextField(blank=True, default='', verbose_name='Ссылка на изображение для аватарки'),
        ),
        migrations.AddField(
            model_name='users',
            name='money_earned',
            field=models.IntegerField(default=0, verbose_name='Заработок на продажах'),
        ),
        migrations.AddField(
            model_name='users',
            name='money_spend',
            field=models.IntegerField(default=0, verbose_name='Потрачено на покупки'),
        ),
        migrations.AddField(
            model_name='users',
            name='products_purchased',
            field=models.IntegerField(default=0, verbose_name='Количество купленных товаров'),
        ),
        migrations.AddField(
            model_name='users',
            name='products_sold',
            field=models.IntegerField(default=0, verbose_name='Колчество проданных товаров'),
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=-1, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_surname',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Фамилия'),
        ),
    ]
