from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from braces.views import AnonymousRequiredMixin
from utils.shortcuts import create_or_render
from utils.views import AuthorRequiredMixin

from .models import User
from .forms import UserCreationForm, UserEditForm


# TODO: Edit password.
# TODO: Forgot your password?
@login_required(login_url='users:login')
def user(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'users/user.html', {'user': user})


class Register(AnonymousRequiredMixin, View):
    template_name = 'users/register.html'
    authenticated_redirect_url = '/'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return create_or_render(request, self.template_name, UserCreationForm)


class EditUser(AuthorRequiredMixin, View):
    template_name = 'users/edit.html'
    model = User

    def get(self, request, user):
        form = UserEditForm(instance=user)
        return render(request, self.template_name, {'user': user, 'form': form})

    def post(self, request, user):
        form = UserEditForm(request.POST, instance=user)
        return create_or_render(request, self.template_name, form)
