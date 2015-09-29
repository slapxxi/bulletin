from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Category


class CategoryTest(TestCase):
  def test_category(self):
    category = Category.objects.create(name='Mobile Phones')
    self.assert_created(Category)
    self.assertEquals(category.name, 'Mobile Phones')

  def assert_created(self, model_class):
    self.assertEquals(model_class.objects.count(), 1)


class CategoryViewsTest(TestCase):
  def test_visiting_categories_page(self):
    response = self.client.get(reverse('categories:index'))
    self.assertTemplateUsed(response, 'categories/index.html')
