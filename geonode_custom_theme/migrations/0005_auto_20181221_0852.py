# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-21 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_custom_theme', '0004_auto_20181221_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedgeonodethemecustomization',
            name='navbar_hover_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='advancedgeonodethemecustomization',
            name='primary_button_hover_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
