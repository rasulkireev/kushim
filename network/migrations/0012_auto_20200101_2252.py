# Generated by Django 2.2.6 on 2020-01-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20191230_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='when_to_contact',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
