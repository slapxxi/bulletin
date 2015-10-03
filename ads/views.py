from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from utils.shortcuts import create_or_render

from .decorators import author_required
from .forms import AdForm
from .models import Ad


def index(request):
  ads = Ad.objects.all().order_by('-published_at')
  return render(request, 'ads/index.html', {'ads': ads})


def show(request, id):
  ad = get_object_or_404(Ad, pk=id)
  return render(request, 'ads/show.html', {'ad': ad})


@author_required
def delete(request, instance):
  instance.delete()
  return redirect('ads:index')


class CreateAd(View):
  @method_decorator(login_required(login_url='users:login'))
  def get(self, request):
    form = AdForm()
    return render(request, 'ads/new.html', {'form': form})

  @method_decorator(login_required(login_url='users:login'))
  def post(self, request):
    form = AdForm(request.POST, instance=Ad(author=request.user))
    return create_or_render(request, 'ads/new.html', form)


class EditAd(View):
  @method_decorator(author_required)
  def get(self, request, ad):
    form = AdForm(instance=ad)
    return render(request, 'ads/edit.html', {'form': form})

  @method_decorator(author_required)
  def post(self, request, ad):
    form = AdForm(request.POST, instance=ad)
    return create_or_render(request, 'ads/show.html', form)


# TODO: Add DeleteView
