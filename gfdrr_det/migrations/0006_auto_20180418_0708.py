# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-18 12:08
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import gfdrr_det.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gfdrr_det', '0005_hevedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='hevedetails',
            name='envelope',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='hevedetails',
            name='dataset_type',
            field=models.CharField(choices=[(b'exposure', b'exposure'), (b'hazard', b'hazard'), (b'vulnerability', b'vulnerability')], max_length=20, validators=[gfdrr_det.validators.validate_dataset_type]),
        ),
    ]