# Generated by Django 3.2.13 on 2022-05-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, verbose_name='Номер телефона'),
        ),
    ]
