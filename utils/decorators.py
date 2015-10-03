from functools import wraps
from nose.tools import nottest


def decorator(decorator_fn):
  @wraps(decorator_fn)
  def _decorator(fn):
    @wraps(fn)
    def _decorated_fn(*args, **kwargs):
      return decorator_fn(fn, *args, **kwargs)
    return _decorated_fn
  return _decorator


@nottest
def test(description):
  def _decorator(fn):
    fn.__name__ = "blah_blah"
    fn.__doc__  = description
    fn.__test__ = True
    return fn
  return _decorator


def use(*setups):
  def _decorator(fn):
    @wraps(fn)
    def _decorated(*args):
      setups_ = [setup() for setup in setups]
      return fn(*setups_)
    return _decorated
  return _decorator
