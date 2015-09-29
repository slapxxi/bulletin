from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Location


class LocationTest(TestCase):
  def test_category(self):
    location = Location.objects.create(name='Saint Petersburg')
    self.assert_created(Location)
    self.assertEquals(location.name, 'Saint Petersburg')

  def assert_created(self, model_class):
    self.assertEquals(model_class.objects.count(), 1)


class LocationsViewsTest(TestCase):
  def test_visiting_categories_page(self):
    response = self.client.get(reverse('locations:index'))
    self.assertTemplateUsed(response, 'locations/index.html')
