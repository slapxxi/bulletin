from django.test import Client, TestCase
from django.shortcuts import resolve_url
from django.core.urlresolvers import reverse

from users.tests.setup import UserSetup
from ads.tests.setup import AdSetup
from ads.models import Ad


class AdvertisementViewsTest(AdSetup, UserSetup, TestCase):
    def setUp(self):
        self.user = self.create_user()

    def test_author_set_automatically(self):
        "Author is set automatically when ad is created."
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(resolve_url(self.user))
        self.assertContains(response, "User's Profile")

    def test_login_required(self):
        "Login required in order to create an advertisement."
        response = self.client.get(reverse('ads:new'))
        self.assertRedirects(response, reverse('users:login')+
            '?next='+reverse('ads:new'))

    def test_updating_advertisement(self):
        "Only authors can update their ads."
        ad = self.create_advertisement(author=self.user)
        response = self.client.get(reverse('ads:edit', args=[ad.id]))
        self.assertRedirects(response, resolve_url(ad))

    def test_deleting_advertisement(self):
        "Only authors can delete their ads."
        ad = self.create_advertisement(author=self.user)
        response = self.client.get(reverse('ads:delete', args=[ad.id]))
        self.assertRedirects(response, resolve_url(ad))
