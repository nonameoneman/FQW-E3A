# Generated by Django 3.2.13 on 2022-06-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0024_auto_20220613_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline_reg',
            name='send',
            field=models.BooleanField(default=False, verbose_name='Отправить советнику'),
        ),
    ]