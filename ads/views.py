from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from utils.shortcuts import create_or_render

from .forms import AdForm
from .models import Ad


def index(request):
  ads = Ad.objects.all().order_by('-published_at')
  return render(request, 'ads/index.html', {'ads': ads})


def show(request, id):
  ad = get_object_or_404(Ad, pk=id)
  return render(request, 'ads/show.html', {'ad': ad})


class CreateAd(View):
  @method_decorator(login_required(login_url='users:login'))
  def get(self, request):
    form = AdForm()
    return render(request, 'ads/new.html', {'form': form})

  @method_decorator(login_required(login_url='users:login'))
  def post(self, request):
    form = AdForm(request.POST, instance=Ad(author=request.user))
    return create_or_render(request, 'ads/new.html', form)


def categories(request):
  return render(request, 'ads/categories.html')


def locations(request):
  return render(request, 'ads/locations.html')

# TODO: Add UpdateView
# TODO: Add DeleteView
