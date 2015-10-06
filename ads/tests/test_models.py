from datetime import datetime

from django.core.exceptions import ValidationError

from nose import with_setup
from nose.tools import ok_, eq_, raises

from utils.decorators import use, teardown
from users.tests.setup import create_user, destroy_users
from ads.models import Ad


@use(create_user)
@teardown(destroy_users)
def test_str_representation(user):
  "An ad string representation."
  ad = Ad.objects.create(title='test ad', author=user)
  eq_(str(ad), '"test ad" by user')


@use(create_user)
@teardown(destroy_users)
def test_published_at(user):
  "Published_at is auto_created on save."
  ad = Ad.objects.create(author=user)
  ok_(isinstance(ad.published_at, datetime))


@use(create_user)
@teardown(destroy_users)
@raises(ValidationError)
def test_price_validation(user):
  "Price can't be lower than required."
  ad = Ad.objects.create(title='test',
                         author=user,
                         description='*'*61,
                         price=-1)
  ad.clean_fields()
