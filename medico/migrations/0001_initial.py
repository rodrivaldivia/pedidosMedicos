# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-04 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]