from django.core.urlresolvers import reverse
from django.test import TestCase


class RegisterTest(TestCase):
  def test_visitors_can_register(self):
    response = self.client.get(reverse('users:register'))
    self.assertTemplateUsed(response, 'users/register.html')

  def test_missing_email(self):
    data = {
      'username': 'slava',
      'password': 'password',
      'password_confirmation': 'password',
    }
    response = self.client.post(reverse('users:register'), data=data)
    self.assertContains(response, 'Email is required.')
