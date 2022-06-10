# Generated by Django 3.2.13 on 2022-06-10 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0021_auto_20220609_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline_reg',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='disc', to='app_disciplines.disciplines', verbose_name='Название дисциплины'),
        ),
    ]
