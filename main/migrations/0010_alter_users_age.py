# Generated by Django 4.1.5 on 2023-03-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_users_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(blank=True, default='', verbose_name='Возраст'),
        ),
    ]