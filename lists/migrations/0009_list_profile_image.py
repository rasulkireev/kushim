# Generated by Django 2.2.6 on 2019-12-31 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20191227_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='garden-desc-image/'),
        ),
    ]
