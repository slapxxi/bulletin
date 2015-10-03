from django.forms import ModelForm
from django.shortcuts import redirect, render


def create_or_render(request, template_name, form):
  """Creates an object or renders the form with errors."""
  if not isinstance(form, ModelForm):
    form = form(request.POST)
  if form.is_valid():
    instance = form.save()
    return redirect(instance)
  else:
    return render(request, template_name, {'form': form})
