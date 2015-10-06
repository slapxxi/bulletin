from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from braces.views import AnonymousRequiredMixin
from utils.shortcuts import create_or_render

from .models import User
from .forms import UserCreationForm


@login_required(login_url='users:login')
def user(request, id):
  user = get_object_or_404(User, pk=id)
  return render(request, 'users/user.html', {'user': user})


class Register(AnonymousRequiredMixin, View):
  authenticated_redirect_url = '/'

  def get(self, request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

  def post(self, request):
    return create_or_render(request, 'users/register.html', UserCreationForm)
