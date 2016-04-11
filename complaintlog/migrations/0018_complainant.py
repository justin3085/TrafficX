# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaintlog', '0017_delete_complainant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complainant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_name', models.ForeignKey(to='complaintlog.Complaint', to_field=b'')),
            ],
        ),
    ]
