# Generated by Django 2.2.6 on 2019-11-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20191028_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='listentry',
            name='support_image',
            field=models.ImageField(blank=True, upload_to='list-support-images/'),
        ),
    ]
