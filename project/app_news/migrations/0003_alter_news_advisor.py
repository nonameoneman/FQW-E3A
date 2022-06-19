# Generated by Django 3.2.13 on 2022-06-14 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0019_groups_department'),
        ('app_news', '0002_news_hide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='advisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_users.advisor', verbose_name='Советник'),
        ),
    ]