# Generated by Django 3.2 on 2021-04-25 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Todo',
        ),
    ]
