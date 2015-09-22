# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(editable=False, default='RUB', max_length=3, choices=[('RUB', 'Russian Ruble'), ('USD', 'US Dollar')]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=djmoney.models.fields.MoneyField(max_digits=10, decimal_places=2, default=Decimal('0.0'), default_currency='RUB'),
        ),
    ]
