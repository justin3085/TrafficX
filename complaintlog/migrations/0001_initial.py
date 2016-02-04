# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complaintType', models.CharField(max_length=25, verbose_name=b'Complaint Type')),
                ('dateofcomplaint', models.DateField(verbose_name=b'Date of Complaint')),
                ('street', models.CharField(max_length=100, verbose_name=b'Street')),
                ('xstreet', models.CharField(max_length=100, verbose_name=b'Cross Street', blank=True)),
                ('description', models.TextField(verbose_name=b'Description')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
