from functools import wraps
from django.shortcuts import redirect

def anonymous_required(fn):
  """
  Decorator that requires a user to be anonymous
  to proceed.
  """
  @wraps(fn)
  def wrapped_fn(request, *args, **kwargs):
    if request.user.is_authenticated():
      return redirect('users:user', request.user.id)
    return fn(request, *args, **kwargs)
  return wrapped_fn
