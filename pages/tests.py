from django.core.urlresolvers import resolve
from django.test import TestCase

from . import views


class PagesTest(TestCase):
  def test_root_url_resolves_to_index_view(self):
    view = resolve('/')
    self.assertEqual(view.func, views.index)

  def test_about_url_resolves_to_about_view(self):
    view = resolve('/about/')
    self.assertEqual(view.func, views.about)
