from django.shortcuts import render

from .models import Category


def index(request):
  return render(request, 'categories/index.html')
