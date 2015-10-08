from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Category


class CategoryTest(TestCase):
    def test_category(self):
        category = self.create_category()
        self.assert_created(Category)
        self.assertEquals(category.name, 'Test Category')

    def test_str_representation(self):
        category = self.create_category()
        self.assertEquals(str(category), 'Test Category')
        self.assertEquals(repr(category), '<Category: Test Category>')

    def create_category(self, name='Test Category'):
        category = Category.objects.create(name=name)
        return category

    def assert_created(self, model_class):
        self.assertEquals(model_class.objects.count(), 1)


class CategoryViewsTest(TestCase):
    def test_visiting_categories_page(self):
        response = self.client.get(reverse('categories:index'))
        self.assertTemplateUsed(response, 'categories/index.html')
