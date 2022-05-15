# Generated by Django 3.2.13 on 2022-05-15 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0007_advisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='user_id',
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='ID Пользователя'),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='position',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
    ]
