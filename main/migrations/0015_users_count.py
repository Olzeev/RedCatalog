# Generated by Django 4.1.5 on 2023-03-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_users_img_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество товара (в шк)'),
        ),
    ]
