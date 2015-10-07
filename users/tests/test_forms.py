from django.test import TestCase

from users.tests.setup import UserSetup
from users.forms import UserCreationForm
from users.models import User


class UserCreationFormTest(UserSetup, TestCase):
  def setUp(self):
    self.valid_data = {
      'username': 'user',
      'email': 'user@mail.com',
      'password': 'password',
      'password_confirmation': 'password',
    }

  def test_creating_user(self):
    form = UserCreationForm(self.valid_data)
    self.assertIsInstance(form.save(), User)

  def test_username_unique(self):
    self.create_user()
    form = UserCreationForm(self.valid_data)
    self.assertIn('A user with that username already exists.',
                   form.errors['username'])

  def test_email_required(self):
    self.valid_data.pop('email')
    form = UserCreationForm(self.valid_data)
    self.assertIn('Email is required.', form.errors['email'])

  def test_username_required(self):
    self.valid_data.pop('username')
    form = UserCreationForm(self.valid_data)
    self.assertIn('This field is required.', form.errors['username'])

  def test_password_required(self):
    self.valid_data.pop('password')
    form = UserCreationForm(self.valid_data)
    self.assertIn('This field is required.', form.errors['password'])
