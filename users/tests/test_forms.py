from django.test import TestCase

from users.forms import  UserCreationForm
from users.models import User


class UserCreationFormTest(TestCase):
  def setUp(self):
    self.valid_data = {
      'username': 'user',
      'email': 'user@mail.com',
      'password': 'password',
      'password_confirmation': 'password',
    }

  def test_creating_user(self):
    form = UserCreationForm(data=self.valid_data)
    self.assertIsInstance(form.save(), User)

  def test_email_required(self):
    self.valid_data.pop('email')
    form = UserCreationForm(data=self.valid_data)
    self.assertRaises(ValueError, lambda: form.save())

  def test_username_required(self):
    self.valid_data.pop('username')
    form = UserCreationForm(data=self.valid_data)
    self.assertRaises(ValueError, lambda: form.save())

  def test_password_required(self):
    self.valid_data.pop('password')
    form = UserCreationForm(data=self.valid_data)
    self.assertRaises(ValueError, lambda: form.save())
