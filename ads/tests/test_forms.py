from django.test import TestCase

from users.tests.setup import UserSetup
from ads.tests.setup import AdSetup
from ads.models import Ad
from ads.forms import AdForm


class AdFormTest(AdSetup, UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user()
        self.ad = self.create_advertisement(author=self.user)
        self.data = {
            'title': self.ad.title,
            'description': self.ad.description,
            'price_0': 100,
            'price_1': 'USD',
        }

    def test_updating_published_at(self):
        "Published_at is not updated after creating."
        published_at = self.ad.published_at
        form = AdForm(self.data, instance=self.ad)
        instance = form.save()
        self.assertEquals(instance.published_at, published_at)
