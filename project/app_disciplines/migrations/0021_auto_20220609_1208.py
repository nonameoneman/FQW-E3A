# Generated by Django 3.2.13 on 2022-06-09 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0020_alter_department_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplines',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_disciplines.department', verbose_name='Отделение'),
        ),
        migrations.AlterField(
            model_name='disciplines',
            name='form_control',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_disciplines.form_controls', verbose_name='Форма контроля'),
        ),
    ]