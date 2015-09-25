from django.forms import Form, ModelForm
from django.shortcuts import redirect, render


def create_or_render(request, template_name, form):
  # Check if form is a form class
  if not isinstance(form, ModelForm):
    form = form(request.POST)
  if form.is_valid():
    instance = form.save()
    return redirect(instance)
  else:
    return render(request, template_name, {'form': form})
