# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='dni',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nro_afiliado',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
