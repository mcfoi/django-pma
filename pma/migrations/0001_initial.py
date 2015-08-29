# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_camp', models.CharField(unique=True, max_length=7)),
                ('codice_p', models.CharField(max_length=13)),
                ('data_c', models.DateTimeField(null=True, blank=True)),
                ('data_r', models.DateTimeField(null=True, blank=True)),
                ('quota_f', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('nr', models.IntegerField()),
                ('data_cons', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'camp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forn', models.TextField()),
            ],
            options={
                'db_table': 'forn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FornCamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'forn_camp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc', models.DecimalField(null=True, max_digits=5, decimal_places=3, blank=True)),
                ('mdl', models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)),
                ('metodo', models.TextField(null=True, blank=True)),
                ('data', models.DateTimeField()),
            ],
            options={
                'db_table': 'lim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='M',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_val', models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)),
                ('t_val', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(unique=True, max_length=4)),
                ('descr', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'monit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Par',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('par', models.TextField()),
                ('unit', models.TextField(null=True, blank=True)),
                ('matr', models.TextField()),
                ('analisi', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'par',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prof', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'prof',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('codice', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('data_r', models.DateTimeField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=102092, null=True, blank=True)),
            ],
            options={
                'db_table': 'punto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descr', models.TextField(null=True, blank=True)),
                ('pma', models.IntegerField()),
                ('y', models.DecimalField(max_digits=10, decimal_places=3)),
                ('x', models.DecimalField(max_digits=10, decimal_places=3)),
                ('lat', models.TextField()),
                ('lon', models.TextField()),
                ('quota', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('foto', models.TextField(null=True, blank=True)),
                ('log', models.TextField(null=True, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sito',
                'managed': False,
            },
        ),
    ]
