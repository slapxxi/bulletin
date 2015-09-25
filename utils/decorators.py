from functools import wraps


def decorator(decorator_fn):
  @wraps(decorator_fn)
  def _decorator(fn):
    @wraps(fn)
    def _decorated_fn(*args, **kwargs):
      return decorator_fn(fn, *args, **kwargs)
    return _decorated_fn
  return _decorator
