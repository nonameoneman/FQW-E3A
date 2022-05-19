# Generated by Django 3.2.13 on 2022-05-19 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0007_disciplines_period'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline_reg',
            options={'ordering': ['discipline', 'date_of_reg'], 'verbose_name': 'Регистрацию на предмет', 'verbose_name_plural': 'Регистрации на предметы'},
        ),
        migrations.AlterModelOptions(
            name='disciplines',
            options={'ordering': ['name', 'period'], 'verbose_name': 'Дисциплину', 'verbose_name_plural': 'Дисциплины'},
        ),
        migrations.CreateModel(
            name='Credits_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_half', models.IntegerField(verbose_name='Первое полугодие')),
                ('second_half', models.IntegerField(verbose_name='Второе полугодие')),
                ('extra', models.IntegerField(verbose_name='Дополнительно')),
                ('total', models.IntegerField(verbose_name='Всего кредитов')),
                ('dis_reg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_disciplines.discipline_reg', verbose_name='Зарегистрированные предметы')),
            ],
        ),
    ]