from django.core.urlresolvers import resolve
from django.test import TestCase

from nose.tools import eq_

from . import views


def test_root_resolves_to_correct_view():
  view = resolve('/')
  eq_(view.func, views.index)


def test_about_resolves_to_correct_view():
  view = resolve('/about/')
  eq_(view.func, views.about)
