from django.test import TestCase

from users.models import User


class UserTest(TestCase):
  # TODO: Add contact information.
  # TODO: Email should be unique.
  def setUp(self):
    self.user = User.objects.create()

  def test_get_absolute_url(self):
    url = self.user.get_absolute_url()
    self.assertEqual(url, '/user/1/')
