# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 21:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170327_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='like',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 2, 21, 7, 19, 260065)),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='like',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
