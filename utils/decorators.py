from functools import wraps
from nose import with_setup
from nose.tools import nottest


def decorator(decorator_fn):
    @wraps(decorator_fn)
    def _decorator(fn):
        @wraps(fn)
        def _decorated_fn(*args, **kwargs):
          return decorator_fn(fn, *args, **kwargs)
        return _decorated_fn
    return _decorator


def use(*setups):
    def _decorator(fn):
        @wraps(fn)
        def _decorated(*args):
            setups_ = [setup() for setup in setups]
            return fn(*setups_)
        return _decorated
    return _decorator


def teardown(teardown_):
    return with_setup(teardown=teardown_)
