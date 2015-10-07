from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from nose import with_setup
from nose.tools import eq_

from utils.decorators import use, teardown
from ads.models import Ad
from users.models import User
from users.tests.setup import create_user
from .models import Location


def create_client():
    return Client()

def create_location():
    return Location.objects.create(name='Moscow')

def destroy_locations():
    return Location.objects.all().delete()


@use(create_location)
@teardown(destroy_locations)
def test_create_a_location(location):
    "Creating a location."
    eq_(Location.objects.count(), 1)


@use(create_client)
def test_all_locations(client):
    "Listing all locations."
    response = client.get(reverse('locations:index'))
    eq_(response.status_code, 200)


@use(create_location, create_client)
@teardown(destroy_locations)
def test_even_more(location, client):
    "Showing advertisement associated with a location."
    response = client.get(reverse('locations:ads', args=[location.slug]))
    eq_(response.status_code, 200)


@use(create_user, create_location)
@teardown(destroy_locations)
def test_rest(user, location):
    "Creating an ad with a location."
    ad = Ad.objects.create(author=user, location=location)
    eq_(location.ad_set.first(), ad)
