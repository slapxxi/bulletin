from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import User
from .forms import UserCreationForm
from . import anonymous_required


@login_required(login_url='users:login')
def user(request, id):
  user = get_object_or_404(User, pk=id)
  return render(request, 'users/user.html', {'user': user})


class Register(CreateView):
  template_name = 'users/register.html'
  form_class = UserCreationForm

  get = method_decorator(anonymous_required)(CreateView.get)
  post = method_decorator(anonymous_required)(CreateView.post)
