# Generated by Django 3.2.12 on 2022-05-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_status',
            field=models.IntegerField(default=1),
        ),
    ]