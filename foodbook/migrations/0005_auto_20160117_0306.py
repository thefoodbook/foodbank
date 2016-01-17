# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodbook', '0004_auto_20160117_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=600, null=True, blank=True)),
                ('location', models.CharField(max_length=600, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_tags', models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True)),
                ('favorite_restaurants', models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User_Profile',
        ),
        migrations.AlterField(
            model_name='image',
            name='restaurant_key',
            field=models.ForeignKey(blank=True, to='foodbook.Restaurant', null=True),
        ),
    ]
