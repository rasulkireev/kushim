# Generated by Django 2.2.6 on 2019-11-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='portfolio_image',
            field=models.ImageField(blank=True, upload_to='profile-images/'),
        ),
    ]
