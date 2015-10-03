from django.shortcuts import render

from .models import Location


def index(request):
  return render(request, 'locations/index.html')


def ads(request, slug):
  location = Location.objects.get(slug=slug)
  ads      = location.ad_set.all()
  context  = {'ads': ads, 'location': location}
  return render(request, 'locations/ads.html', context)
