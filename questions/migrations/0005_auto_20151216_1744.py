# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 23:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151216_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_choice',
            field=models.CharField(default=datetime.datetime(2015, 12, 16, 23, 44, 4, 600259, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='first_choice',
            field=models.CharField(default=datetime.datetime(2015, 12, 16, 23, 44, 33, 656224, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='second_choice',
            field=models.CharField(default=datetime.datetime(2015, 12, 16, 23, 44, 39, 632020, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='third_choice',
            field=models.CharField(default=datetime.datetime(2015, 12, 16, 23, 44, 53, 264069, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
