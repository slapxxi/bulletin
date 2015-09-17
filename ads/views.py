from django.shortcuts import render


def index(request):
  return render(request, 'ads/index.html')


def categories(request):
  return render(request, 'ads/categories.html')


def locations(request):
  return render(request, 'ads/locations.html')
