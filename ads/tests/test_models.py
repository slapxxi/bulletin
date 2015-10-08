from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from users.tests.setup import UserSetup
from ads.tests.setup import AdSetup
from ads.models import Ad


class AdvertisementTest(AdSetup, UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user()

    def test_price_min_value(self):
        "Price can't be lower than required."
        ad = self.create_advertisement(author=self.user, price=-100)
        with self.assertRaises(ValidationError):
            ad.clean_fields()

    def test_published_at_auto_created(self):
        "Published_at field is auto created."
        ad = Ad.objects.create(author=self.user)
        self.assertIsInstance(ad.published_at, datetime)

    def test_is_author(self):
        ad = Ad.objects.create(author=self.user)
        self.assertTrue(ad.is_author(self.user))

    def test_str_representation(self):
        ad = Ad(title="test", author=self.user)
        self.assertEquals(str(ad), 'test')
        self.assertEquals(repr(ad), '<Ad: test>')
