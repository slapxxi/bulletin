from django.test import TestCase
from django.shortcuts import resolve_url

from users.tests.setup import UserSetup
from users.models import User


class UserTest(UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user()

    def test_get_absolute_url(self):
        url = resolve_url(self.user)
        self.assertEqual(url, '/user/1/')
