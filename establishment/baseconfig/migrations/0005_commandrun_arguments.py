# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 22:39
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0004_auto_20170815_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandrun',
            name='arguments',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
