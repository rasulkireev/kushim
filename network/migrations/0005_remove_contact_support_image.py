# Generated by Django 2.2.6 on 2019-11-27 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_contact_support_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='support_image',
        ),
    ]
