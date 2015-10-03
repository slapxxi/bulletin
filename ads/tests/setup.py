from users.tests.setup import user
from ads.models import Ad


def create_ad():
  return Ad.objects.create(author=user())

def ad():
  return Ad.objects.first()
