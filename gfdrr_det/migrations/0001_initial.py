# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################
# Generated by Django 1.9.13 on 2018-03-01 18:49
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import gfdrr_det.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeDivision',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.IntegerField(db_index=True)),
                ('level', models.IntegerField(db_index=True)),
                ('iso', models.CharField(db_index=True, max_length=10)),
                ('iso_id', models.IntegerField(db_index=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('name_eng', models.CharField(blank=True, max_length=50, null=True)),
                ('name_fao', models.CharField(blank=True, max_length=50, null=True)),
                ('name_local', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=80, null=True)),
                ('engtype', models.CharField(blank=True, max_length=80, null=True)),
                ('contains', models.CharField(blank=True, max_length=255, null=True)),
                ('sovereign', models.CharField(blank=True, max_length=50, null=True)),
                ('fips', models.CharField(blank=True, max_length=50, null=True)),
                ('unregion', models.CharField(blank=True, max_length=50, null=True)),
                ('ison', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('valid_from', models.CharField(blank=True, max_length=50, null=True)),
                ('valid_to', models.CharField(blank=True, max_length=50, null=True)),
                ('population', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('sqkm', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('pop_sqkm', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('shape_leng', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('shape_area', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('geom', models.TextField()),
                ('srid', models.IntegerField(default=4326)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='gfdrr_det.AdministrativeDivision')),
            ],
            options={
                'ordering': ['iso', 'name', 'iso_id'],
                'db_table': 'explorationtool_administrativedivision',
                'verbose_name_plural': 'DET Administrative Divisions',
            },
            bases=(gfdrr_det.models.Exportable, models.Model),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('level', models.IntegerField(db_index=True)),
                ('administrative_divisions', models.ManyToManyField(related_name='administrative_divisions', to=b'gfdrr_det.AdministrativeDivision')),
            ],
            options={
                'ordering': ['name', 'level'],
                'db_table': 'explorationtool_region',
                'verbose_name_plural': 'DET Regions',
            },
        ),
        migrations.AddField(
            model_name='administrativedivision',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gfdrr_det.Region'),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='ison',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='pop_sqkm',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='population',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_area',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_leng',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='sqkm',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='ison',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='pop_sqkm',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='population',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_area',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_leng',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='sqkm',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='ison',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='pop_sqkm',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='population',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_area',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='shape_leng',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='sqkm',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=21, null=True),
        ),
    ]
