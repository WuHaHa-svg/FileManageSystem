# Generated by Django 3.2.12 on 2022-05-27 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0011_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
