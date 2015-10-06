from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from braces.views import LoginRequiredMixin
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
def delete(_request, advertisement):
  advertisement.delete()
  return redirect('ads:index')


class CreateAd(LoginRequiredMixin, View):
  template_name = 'ads/new.html'
  login_url = 'users:login'

  def get(self, request):
    form = AdForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request):
    ad_with_author = Ad(author=request.user)
    form = AdForm(request.POST, instance=ad_with_author)
    return create_or_render(request, self.template_name, form)


class EditAd(View):
  @method_decorator(author_required)
  def get(self, request, ad):
    form = AdForm(instance=ad)
    return render(request, 'ads/edit.html', {'form': form})

  @method_decorator(author_required)
  def post(self, request, ad):
    form = AdForm(request.POST, instance=ad)
    return create_or_render(request, 'ads/show.html', form)
