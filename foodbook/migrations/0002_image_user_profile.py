# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.CharField(max_length=600)),
                ('image_tags', models.CommaSeparatedIntegerField(max_length=200)),
                ('image_text', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_profile_name', models.CharField(max_length=200)),
                ('image_tags', models.CommaSeparatedIntegerField(max_length=200)),
                ('favorite_restaurants', models.CommaSeparatedIntegerField(max_length=200)),
            ],
        ),
    ]
