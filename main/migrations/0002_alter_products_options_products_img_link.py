# Generated by Django 4.1.7 on 2023-03-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='products',
            name='img_link',
            field=models.TextField(default='', verbose_name='Ссылка на изображение'),
        ),
    ]
