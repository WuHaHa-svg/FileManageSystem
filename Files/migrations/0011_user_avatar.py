# Generated by Django 3.2.12 on 2022-05-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0010_file_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='', max_length=100),
        ),
    ]