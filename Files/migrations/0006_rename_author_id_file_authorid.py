# Generated by Django 3.2.12 on 2022-05-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0005_auto_20220526_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='author_id',
            new_name='authorId',
        ),
    ]
