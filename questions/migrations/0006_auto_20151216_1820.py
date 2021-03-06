# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20151216_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.CharField(help_text='This MUST be the correct answer', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='first_line',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='last_line',
            field=models.CharField(blank=True, help_text='Use this line to create multiple line question', max_length=200),
        ),
    ]
