from django.test import TestCase
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url

from users.tests.setup import UserSetup
from users.models import User


class RegisterTest(UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user('user', 'password')
        self.valid_user_data = {
            'username': 'slava',
            'email': 'user@mail.com',
            'password': 'password',
            'password_confirmation': 'password',
        }

    def test_correct_template_used(self):
        response = self.client.get(resolve_url('users:register'))
        self.assertTemplateUsed(response, 'users/register.html')

    def test_redirects_if_authenticated(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(resolve_url('users:register'))
        self.assertRedirects(response, resolve_url('pages:index'))

    def test_registration(self):
        response = self.client.post(resolve_url('users:register'), self.valid_user_data)
        self.assertRedirects(response, 'user/2/', target_status_code=302)

    def test_missing_email(self):
        self.valid_user_data.pop('email')
        invalid_data = self.valid_user_data
        response = self.client.post(resolve_url('users:register'), data=invalid_data)
        self.assertContains(response, 'Email is required.')


class EditTest(UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user('test_user')
        self.url = resolve_url('users:edit', self.user.id)

    def test_updating_profile(self):
        self.login()
        response = self.client.post(self.url, {
            'email': self.user.email,
            'phone_number': '+79313333333',
        })
        user = User.objects.first()
        self.assertEquals(str(user.phone_number), '+79313333333')

    def test_only_owners_can_edit_their_profiles(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, resolve_url(self.user), target_status_code=302)

    def login(self):
        username = self.user.username
        password = 'password'
        return self.client.login(username=username, password=password)
