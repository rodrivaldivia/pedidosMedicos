# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0010_auto_20180207_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='CABA', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='CABA', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Provincia'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='localidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedido.Localidad'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedido.Provincia'),
        ),
    ]
