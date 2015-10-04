from nose import with_setup
from nose.tools import ok_, eq_, raises

from django.test import Client
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from utils.decorators import test, use
from users.tests.setup import create_user, destroy_users

from ads.models import Ad
from ads.forms import AdForm


@with_setup(teardown=destroy_users)
@use(create_user)
@test("Published_at can't be updated after creating.")
def dont_update(user):
  data = {'description': '*'*61, 'title': 'test', 'price_0': 100, 'price_1': 'USD'}
  form = AdForm(data, instance=Ad(author=user))
  ad = form.save()
  published_at = ad.published_at
  data.update({'published_at': timezone.now()})
  form = AdForm(data, instance=ad)
  form.save()
  eq_(ad.published_at, published_at)
