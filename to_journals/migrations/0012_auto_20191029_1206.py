# Generated by Django 2.2.6 on 2019-10-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_journals', '0011_auto_20191029_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_journal_entry',
            name='body',
            field=models.TextField(),
        ),
    ]
