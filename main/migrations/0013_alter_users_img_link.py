# Generated by Django 4.1.5 on 2023-03-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_users_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='img_link',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='Ссылка на изображение для аватарки'),
        ),
    ]
