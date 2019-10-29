# Generated by Django 2.2.6 on 2019-10-28 16:36

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=40)),
                ('list_slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='list_name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('list_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
                ('list_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]