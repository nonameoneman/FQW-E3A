# Generated by Django 3.2.13 on 2022-06-14 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0019_groups_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('date_of_pub', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.advisor', verbose_name='Советник')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['date_of_pub'],
            },
        ),
    ]