# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-12 12:00
from __future__ import unicode_literals

from django.db import migrations, models


def forward_func(*args):
	create_countries()


def reverse_func(*args):
	pass


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('iso_code', models.CharField(max_length=2, unique=True)),
                ('iso3_code', models.CharField(max_length=3, unique=True)),
                ('phone_number_prefix', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
    ]
