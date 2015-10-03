from nose import with_setup
from nose.tools import ok_, eq_
from django.http import HttpResponse

from django.test import Client
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from utils.decorators import test, use
from users.tests.setup import create_user, destroy_user, user, destroy_users

from ads.models import Ad


def create_client():
  return Client()


@use(create_client, create_user)
@with_setup(teardown=destroy_users)
@test("Author is set automatically on save.")
def set_author(client, user):
  print(client.login(username=user.username, password='password'))
  response = client.post(reverse('ads:new'), data={
    'title': 'new title',
    'description': '*'*61,
    'price_0': 100,
    'price_1': 'RUB',
  })
  eq_(Ad.objects.count(), 1)
  ok_(isinstance(response, HttpResponseRedirect))


@use(create_client, create_user)
@with_setup(destroy_users)
@test("Delete via HTTP.")
def delete_ad(client, user):
  client.login(username=user.username, password='password')
  ad = Ad.objects.create(author=user)
  response = client.get(reverse('ads:delete', args=[ad.id]))
  ok_(isinstance(response, HttpResponseRedirect))


@use(create_client)
@with_setup(destroy_users)
@test("Loging required in order to create ads.")
def login_required(client):
  response = client.get(reverse('ads:new'))
  ok_(isinstance(response, HttpResponseRedirect))
