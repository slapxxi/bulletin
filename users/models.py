from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  # TODO: Add contact information
  def get_absolute_url(self):
    return reverse('users:user', args=(self.id,))
