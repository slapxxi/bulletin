from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    # TODO: Add user location.
    # TODO: Send email to activate user profile.
    phone_number = PhoneNumberField(blank=True)

    def get_absolute_url(self):
        return reverse('users:user', args=(self.id,))

    def is_author(self, user):
        return self.id == user.id
