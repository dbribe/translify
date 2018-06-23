# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 01:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translifyapp', '0005_auto_20180510_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='texttranslation',
            name='title',
            field=models.CharField(default='Test', max_length=256),
        ),
        migrations.AddField(
            model_name='texttranslation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
