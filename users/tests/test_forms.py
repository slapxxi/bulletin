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
    form = self._create_form(self.valid_data)
    self.assertIsInstance(form.save(), User)

  def test_username_unique(self):
    self._create_user(self.valid_data)
    form = self._create_form(self.valid_data)
    self.assertIn('A user with that username already exists.',
                   form.errors['username'])

  def test_email_required(self):
    self.valid_data.pop('email')
    form = self._create_form(self.valid_data)
    self.assertIn('Email is required.', form.errors['email'])

  def test_username_required(self):
    self.valid_data.pop('username')
    form = self._create_form(self.valid_data)
    self.assertIn('This field is required.', form.errors['username'])

  def test_password_required(self):
    self.valid_data.pop('password')
    form = self._create_form(self.valid_data)
    self.assertIn('This field is required.', form.errors['password'])

  def _create_form(self, data):
    return UserCreationForm(data=data)

  def _create_user(self, data):
    user = User.objects.create(username=data['username'])
    user.set_password(data['password'])
    user.save()
    return user
