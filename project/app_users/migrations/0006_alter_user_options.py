# Generated by Django 3.2.13 on 2022-05-06 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-is_superuser', '-is_advisor', 'full_name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]