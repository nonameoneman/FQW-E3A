# Generated by Django 3.2.13 on 2022-05-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0013_discipline_reg_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline_reg',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='discipline_reg',
            name='abon',
            field=models.BooleanField(default=False, verbose_name='Отказываю'),
        ),
        migrations.AddField(
            model_name='discipline_reg',
            name='conf',
            field=models.BooleanField(default=False, verbose_name='Подтверждаю'),
        ),
    ]