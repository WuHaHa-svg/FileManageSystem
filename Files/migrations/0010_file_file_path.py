# Generated by Django 3.2.12 on 2022-05-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0009_file_file_lenth'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]