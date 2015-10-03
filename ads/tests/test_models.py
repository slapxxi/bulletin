from datetime import datetime

from nose import with_setup
from nose.tools import ok_, eq_, raises

from django.core.exceptions import ValidationError
from django.utils import timezone

from utils.decorators import test
from users.tests.setup import create_user, destroy_user, user
from ads.models import Ad


@with_setup(create_user, destroy_user)
@test("Published_at is auto-created on save")
def auto_created():
  ad = Ad.objects.create(author=user())
  ok_(isinstance(ad.published_at, datetime))


@with_setup(create_user, destroy_user)
@test("Published_at can't be updated after creating.")
def dont_update():
  ad = Ad.objects.create(author=user())
  published_at = ad.published_at
  ad.published_at = timezone.now()
  ok_(ad.published_at)


@with_setup(create_user, destroy_user)
@raises(ValidationError)
@test("Price can't be lower than required.")
def price_validation():
  ad = Ad.objects.create(author=user())
  ad.full_clean()
