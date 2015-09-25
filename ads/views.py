from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    return self.render(request)

  @method_decorator(login_required(login_url='users:login'))
  def post(self, request):
    form = AdForm(request.POST, instance=Ad(author=request.user))
    if form.is_valid():
      ad = form.save()
      return redirect(ad)
    else:
      return self.render(request, {'form': form})

  def render(self, request, context=None):
    if context is None:
      context = {'form': AdForm()}
    return render(request, 'ads/new.html', context)


def categories(request):
  return render(request, 'ads/categories.html')


def locations(request):
  return render(request, 'ads/locations.html')

# TODO: Add UpdateView
# TODO: Add DeleteView
