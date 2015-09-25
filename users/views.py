from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .decorators import anonymous_required
from .models import User
from .forms import UserCreationForm


@login_required(login_url='users:login')
def user(request, id):
  user = get_object_or_404(User, pk=id)
  return render(request, 'users/user.html', {'user': user})


class Register(View):
  @method_decorator(anonymous_required)
  def get(self, request):
    form = UserCreationForm()
    return self.render(request, {'form': form})

  @method_decorator(anonymous_required)
  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      return redirect(user)
    else:
      return self.render(request, {'form': form})

  def render(self, request, context):
    return render(request, 'users/register.html', context)
