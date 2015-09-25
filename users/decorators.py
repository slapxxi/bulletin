from functools import wraps
from django.shortcuts import redirect


def decorator(decorator_fn):
  @wraps(decorator_fn)
  def _decorator(fn):
    @wraps(fn)
    def _decorated_fn(*args, **kwargs):
      return decorator_fn(fn, *args, **kwargs)
    return _decorated_fn
  return _decorator


@decorator
def anonymous_required(view, request, *args, **kwargs):
  """
  View decorator that requires an anonymous user
  to proceed.
  """
  if request.user.is_authenticated():
    return redirect(request.user)
  return view(request, *args, **kwargs)
