# Generated by Django 4.1.5 on 2023-03-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_users_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='img_link',
            field=models.URLField(blank=True, default='', verbose_name='Ссылка на изображение для аватарки'),
        ),
    ]
