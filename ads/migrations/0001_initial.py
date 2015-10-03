# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djmoney.models.fields
from decimal import Decimal
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(60)])),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('published_at', models.DateTimeField()),
                ('price_currency', djmoney.models.fields.CurrencyField(editable=False, choices=[('RUB', 'Russian Ruble'), ('USD', 'US Dollar')], default='RUB', max_length=3)),
                ('price', djmoney.models.fields.MoneyField(validators=[django.core.validators.MinValueValidator(0.01)], default=Decimal('0.0'), decimal_places=2, default_currency='RUB', max_digits=10)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('location', models.ForeignKey(null=True, to='locations.Location')),
            ],
        ),
    ]
