from django.shortcuts import render

from .models import Location


def index(request):
  return render(request, 'locations/index.html')
