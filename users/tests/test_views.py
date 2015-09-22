from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate

from django.test import TestCase

from users.models import User
from users.forms import  UserCreationForm


class RegisterTest(TestCase):
  def setUp(self):
    self.user = _create_user('user', 'password')
    self.valid_user_data = {
      'username': 'slava',
      'email': 'user@mail.com',
      'password': 'password',
      'password_confirmation': 'password',
    }

  def test_visitors_can_register(self):
    response = self.client.get(reverse('users:register'))
    self.assertTemplateUsed(response, 'users/register.html')

  def test_redirects_if_authenticated(self):
    self.client.login(username=self.user.username, password='password')
    response = self.client.get(reverse('users:register'))
    self.assertRedirects(response, 'user/1/')

  def test_registration(self):
    response = self.client.post(reverse('users:register'), self.valid_user_data)
    self.assertRedirects(response, 'user/2/', target_status_code=302)

  def test_missing_email(self):
    self.valid_user_data.pop('email')
    invalid_data = self.valid_user_data
    response = self.client.post(reverse('users:register'), data=invalid_data)
    self.assertContains(response, 'Email is required.')


def _create_user(name, password):
  user = User(username=name)
  user.set_password(password)
  user.save()
  return user
