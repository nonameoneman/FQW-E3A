# Generated by Django 3.2.13 on 2022-06-29 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_disciplines', '0029_auto_20220629_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discipline_reg',
            old_name='bad',
            new_name='bad_mark',
        ),
        migrations.RenameField(
            model_name='discipline_reg',
            old_name='good',
            new_name='good_mark',
        ),
    ]