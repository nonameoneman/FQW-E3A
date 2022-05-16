# Generated by Django 3.2.13 on 2022-05-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0012_auto_20220517_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-cipher', '-id'], 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterField(
            model_name='student',
            name='cipher',
            field=models.CharField(max_length=25, unique=True, verbose_name='Шифр студента'),
        ),
    ]