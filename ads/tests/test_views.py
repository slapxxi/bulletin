from nose import with_setup
from nose.tools import ok_, eq_
from django.http import HttpResponse

from django.test import Client
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from utils.decorators import use, teardown
from users.tests.setup import create_user, destroy_users

from ads.models import Ad


def create_client():
    return Client()


@use(create_client, create_user)
@teardown(destroy_users)
def test_auto_author(client, user):
    "Author is set automatically."
    client.login(username=user.username, password='password')
    response = client.post(reverse('ads:new'), data={
        'title': 'new title',
        'description': '*'*61,
        'price_0': 100,
        'price_1': 'RUB',
    })
    eq_(Ad.objects.count(), 1)
    ok_(isinstance(response, HttpResponseRedirect))


@use(create_client, create_user)
@teardown(destroy_users)
def test_delete_ad(client, user):
    "Deleting an ad via HTTP."
    client.login(username=user.username, password='password')
    ad = Ad.objects.create(author=user)
    response = client.get(reverse('ads:delete', args=[ad.id]))
    ok_(isinstance(response, HttpResponseRedirect))


@use(create_client)
def test_login_required(client):
    "Login required in order to create an ad."
    response = client.get(reverse('ads:new'))
    ok_(isinstance(response, HttpResponseRedirect))
