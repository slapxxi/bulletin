from django.test import TestCase
from django.core.urlresolvers import reverse

from ads.models import Ad
from users.models import User

from .models import Location


class LocationTest(TestCase):
  def test_category(self):
    location = Location.objects.create(name='Saint Petersburg')
    self.assert_created(Location)
    self.assertEquals(location.name, 'Saint Petersburg')

  def assert_created(self, model_class):
    self.assertEquals(model_class.objects.count(), 1)


class LocationsViewsTest(TestCase):
  def setUp(self):
    self.location = Location.objects.create(name='Moscow')
    user = User.objects.create(username='user')
    Ad.objects.create(title='Ad in Moscow', author=user, location=self.location)

  def test_visiting_locations_page(self):
    response = self.client.get(reverse('locations:index'))
    self.assertTemplateUsed(response, 'locations/index.html')

  def test_showing_ads_by_location(self):
    response = self.client.get(reverse('locations:ads', args=[self.location.slug]))
    self.assertContains(response, 'Ad in Moscow')


class AdsByLocationTest(TestCase):
  def setUp(self):
    self.location = Location.objects.create(name='Moscow')
    self.user = User.objects.create(username='user')

  def test_creating_ad_with_location(self):
    ad = Ad.objects.create(author=self.user, location=self.location)
    self.assertEquals(self.location.ad_set.first(), ad)
