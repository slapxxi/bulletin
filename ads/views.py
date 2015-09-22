from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .forms import AdForm
from .models import Ad


def index(request):
  ads = Ad.objects.all().order_by('-published_at')
  return render(request, 'ads/index.html', {'ads': ads})


def show(request, id):
  ad = get_object_or_404(Ad, pk=id)
  return render(request, 'ads/show.html', {'ad': ad})


class CreateAd(CreateView):
  # TODO: Pass the current user's data to the form on POST.
  # TODO: Require login.
  template_name = 'ads/new.html'
  form_class = AdForm


def categories(request):
  return render(request, 'ads/categories.html')


def locations(request):
  return render(request, 'ads/locations.html')

# TODO: Add UpdateView
# TODO: Add DeleteView
