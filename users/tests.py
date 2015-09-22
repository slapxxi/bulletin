from django.core.urlresolvers import reverse
from django.test import TestCase
from django.template.loader import render_to_string
from django.contrib.auth import authenticate

from .models import User


class UserTest(TestCase):
  # TODO: Add contact information.
  # TODO: Email should be unique.
  def setUp(self):
    self.user = User.objects.create()

  def test_get_absolute_url(self):
    url = self.user.get_absolute_url()
    self.assertEqual(url, '/user/1/')


class RegisterTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='user')
    self.user.set_password('password')
    self.user.save()
    self.valid_user_data = {
      'username': 'slava',
      'email': 'user@mail.com',
      'password': 'password',
      'password_confirmation': 'password',
    }

  # TODO: Redirect to user profile if authenticated.
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
    data = {
      'username': 'slava',
      'password': 'password',
      'password_confirmation': 'password',
    }
    response = self.client.post(reverse('users:register'), data=data)
    self.assertContains(response, 'Email is required.')
