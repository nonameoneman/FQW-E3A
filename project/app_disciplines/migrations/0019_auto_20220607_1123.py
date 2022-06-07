# Generated by Django 3.2.13 on 2022-06-07 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0018_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Отделение', 'verbose_name_plural': '2. Отделения'},
        ),
        migrations.AlterModelOptions(
            name='discipline_reg',
            options={'ordering': ['discipline', 'date_of_reg'], 'verbose_name': 'Регистрацию на предмет', 'verbose_name_plural': '5. Регистрации на предметы'},
        ),
        migrations.AlterModelOptions(
            name='disciplines',
            options={'ordering': ['name'], 'verbose_name': 'Дисциплину', 'verbose_name_plural': '4. Дисциплины'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ['-name'], 'verbose_name': 'Факультет', 'verbose_name_plural': '1. Факультеты'},
        ),
        migrations.AlterModelOptions(
            name='form_controls',
            options={'ordering': ['-name'], 'verbose_name': 'Форму контроля', 'verbose_name_plural': '3. Формы контроля'},
        ),
    ]
