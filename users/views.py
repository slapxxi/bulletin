from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login')
def user(request, id):
  user = get_object_or_404(User, pk=id)
  return render(request, 'users/user.html', {'user': user})


class Register(CreateView):
  template_name = 'users/register.html'
  form_class = UserCreationForm
