from django.shortcuts import render

from .models import Category


def index(request):
  context = {'categories': Category.objects.all()}
  return render(request, 'categories/index.html', context)
