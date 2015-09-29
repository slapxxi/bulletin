from django.shortcuts import render

from .models import Location


def index(request):
  context = {'locations': Location.objects.all()}
  return render(request, 'locations/index.html', context)
