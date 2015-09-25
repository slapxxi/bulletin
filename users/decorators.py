from django.shortcuts import redirect
from utils.decorators import decorator


@decorator
def anonymous_required(view, request, *args, **kwargs):
  """
  View decorator that requires an anonymous user to proceed.
  Otherwise it redirects to the current user's page.
  """
  if request.user.is_authenticated():
    return redirect(request.user)
  return view(request, *args, **kwargs)
