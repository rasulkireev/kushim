# Generated by Django 2.2.6 on 2019-10-28 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='list_slug',
            new_name='slug',
        ),
    ]
