# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20151216_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='last_line',
            field=models.TextField(blank=True, help_text='Use this line to create multiple line question', max_length=200),
        ),
    ]
