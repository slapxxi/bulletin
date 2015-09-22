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

  def test_username_unique(self):
    self._create_user(self.valid_data)
    form = UserCreationForm(data=self.valid_data)
    self.assertRaises(ValueError, lambda: form.save())

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

  def _create_user(self, data):
    user = User.objects.create(username=data['username'])
    user.set_password(data['password'])
    user.save()
    return user
