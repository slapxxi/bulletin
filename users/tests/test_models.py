from django.test import TestCase

from users.tests.setup import UserSetup
from users.models import User


class UserTest(UserSetup, TestCase):
  def setUp(self):
    self.user = self.create_user()

  def test_get_absolute_url(self):
    url = self.user.get_absolute_url()
    self.assertEqual(url, '/user/1/')
