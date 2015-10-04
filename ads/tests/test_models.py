from datetime import datetime

from django.core.exceptions import ValidationError

from nose import with_setup
from nose.tools import ok_, eq_, raises

from utils.decorators import test, use
from users.tests.setup import create_user, destroy_users
from ads.models import Ad


@use(create_user)
@with_setup(teardown=destroy_users)
@test("Published_at is auto-created on save")
def auto_created(user):
  ad = Ad.objects.create(author=user)
  ok_(isinstance(ad.published_at, datetime))


@use(create_user)
@with_setup(teardown=destroy_users)
@test("Price can't be lower than required.")
@raises(ValidationError)
def price_validation(user):
  ad = Ad.objects.create(title='test',
                         author=user,
                         description='*'*61,
                         price=-1)
  ad.clean_fields()
