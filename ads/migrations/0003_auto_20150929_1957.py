# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djmoney.models.fields
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20150922_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='RUB', max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], default=Decimal('0.0')),
        ),
    ]
