from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from nose import with_setup
from nose.tools import eq_

from utils.decorators import test, use
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
@with_setup(teardown=destroy_locations)
@test("Creating a location.")
def test_create_a_location(location):
  eq_(Location.objects.count(), 1)


@use(create_client)
@test("Listing all locations.")
def test_more(client):
  response = client.get(reverse('locations:index'))
  eq_(response.status_code, 200)


@use(create_location, create_client)
@with_setup(teardown=destroy_locations)
@test("Showing advertsisements associated with the location.")
def test_even_more(location, client):
  response = client.get(reverse('locations:ads', args=[location.slug]))
  eq_(response.status_code, 200)


@use(create_user, create_location)
@with_setup(teardown=destroy_locations)
@test("Creating ad with location.")
def test_rest(user, location):
  ad = Ad.objects.create(author=user, location=location)
  eq_(location.ad_set.first(), ad)
