# Generated by Django 3.2.12 on 2022-05-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0007_rename_authorid_file_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(default='', max_length=10),
        ),
    ]