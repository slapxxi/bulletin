from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Ad
from users.models import User


class AdTest(TestCase):
  def setUp(self):
    self.valid_ad_data = {
      'title': 'Advertisement',
      'price': 100,
      'description': '*'*60,
      'author': User.objects.create(),
    }

  def test_price_greater_than_minimum(self):
    self.valid_ad_data.update({'price': -1})
    negative_price_data = self.valid_ad_data
    ad_with_negative_price = Ad(**negative_price_data)
    with self.assertRaises(ValidationError):
      ad_with_negative_price.full_clean()


# TODO: Deleting instances
# TODO: Updating instances
