# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-17 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geonode_client', '0004_auto_20180416_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedGeoNodeThemeCustomization',
            fields=[
                ('geonodethemecustomization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geonode_client.GeoNodeThemeCustomization')),
                ('body_bg', models.ImageField(blank=True, null=True, upload_to=b'img/%Y/%m', verbose_name=b'Datasets background')),
                ('navbar_bg', models.ImageField(blank=True, null=True, upload_to=b'img/%Y/%m', verbose_name=b'Navbar background')),
                ('navbar_search_icon_color', models.CharField(default=b'#333333', max_length=10)),
                ('jumbotron_hyperlink_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('big_search_bg', models.ImageField(blank=True, null=True, upload_to=b'img/%Y/%m', verbose_name=b'Big search background')),
                ('big_search_title_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('big_search_hyperlink_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('big_search_search_icon_color', models.CharField(default=b'#333333', max_length=10)),
                ('datasets_bg', models.ImageField(blank=True, null=True, upload_to=b'img/%Y/%m', verbose_name=b'Datasets background')),
                ('datasets_title_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('datasets_icon_color', models.CharField(default=b'#333333', max_length=10)),
                ('datasets_icon_hover_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_title_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_sub_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_icon_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_icon_title_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_icon_hover_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_button_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_button_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('showcase_hyperlink_text_color', models.CharField(default=b'#333333', max_length=10)),
                ('copyright_logo', models.ImageField(blank=True, null=True, upload_to=b'img/%Y/%m', verbose_name=b'Datasets background')),
            ],
            options={
                'ordering': ('date',),
                'verbose_name_plural': 'Advanced Themes',
            },
            bases=('geonode_client.geonodethemecustomization',),
        ),
    ]
