# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbook', '0005_auto_20160117_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=600)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_tags',
        ),
        migrations.AddField(
            model_name='image',
            name='image_tags',
            field=models.ManyToManyField(to='foodbook.Tag'),
        ),
    ]
