# Generated by Django 2.2.4 on 2019-09-13 14:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_journals', '0002_to_journal_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_journal',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name', unique_with=('name',)),
            preserve_default=False,
        ),
    ]
