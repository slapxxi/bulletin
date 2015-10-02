from datetime import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from .models import Ad
from .forms import AdForm
from users.models import User


# TODO: Deleting advertisement.
# TODO: Updating advertisement.
class AdTest(TestCase):
  def setUp(self):
    self.valid_ad_data = {
      'title': 'Advertisement',
      'price': 100,
      'description': '*'*61,
      'author': User.objects.create(),
    }

  def test_price_greater_than_minimum(self):
    self.valid_ad_data.update({'price': -1})
    negative_price_data = self.valid_ad_data
    ad_with_negative_price = Ad(**negative_price_data)
    with self.assertRaises(ValidationError):
      ad_with_negative_price.full_clean()

  def test_published_at_auto_created(self):
    ad = Ad.objects.create(**self.valid_ad_data)
    self.assertTrue(isinstance(ad.published_at, datetime))


class AdFormTest(TestCase):
  def setUp(self):
    user = User.objects.create(username='slava')
    self.data = {
      'title': 'Advertisement',
      'price': 100,
      'description': '*'*61,
      'author': User.objects.create(),
    }
    self.form_data = {
      'title': 'Advertisement',
      'price_0': 100,
      'price_1': 'RUB',
      'description': '*'*61,
      'author': user,
    }
    self.instance = Ad.objects.create(**self.data)

  def test_published_at_not_updated(self):
    published_at = self.instance.published_at
    form = AdForm(self.form_data, instance=self.instance)
    form.save()
    self.assertEquals(form.instance.published_at, published_at)


class CreateAdTest(TestCase):
  def setUp(self):
    self.user = _create_user('user', 'password')
    self.client.login(username=self.user.username, password='password')
    self.valid_data = {
      'title': 'Test Advertisement',
      'description': '*'*61,
      'price_0': '100.1',
      'price_1': 'USD',
    }

  def test_author_set_automatically(self):
    ad = AdForm(self.valid_data)
    response = self.client.post(reverse('ads:new'), self.valid_data)
    self.assertEqual(Ad.objects.count(), 1)
    self.assertRedirects(response, 'ad/1/')

  def test_login_required(self):
    self.client.logout()
    response = self.client.get(reverse('ads:new'))
    self.assertRedirects(response, 'login/?next=/ads/new/')


def _create_user(name, password):
  user = User.objects.create(username=name)
  user.set_password(password)
  user.save()
  return user
