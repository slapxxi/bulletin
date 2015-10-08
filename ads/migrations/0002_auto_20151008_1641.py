# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.ForeignKey(blank=True, null=True, to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
