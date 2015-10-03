from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.urlresolvers import reverse

from djmoney.models.fields import MoneyField

from users.models import User
from categories.models import Category
from locations.models import Location


class Ad(models.Model):
  # TODO: Add ability to add a set of images.
  title        = models.CharField(max_length=120)
  description  = models.TextField(validators=[MinLengthValidator(60),])
  author       = models.ForeignKey(User)
  location     = models.ForeignKey(Location, null=True)
  categories   = models.ManyToManyField(Category)
  image        = models.ImageField(upload_to='img', blank=True)
  published_at = models.DateTimeField()
  price        = MoneyField(max_digits=10, decimal_places=2,
                 default_currency='RUB', validators=[MinValueValidator(0.01)])

  def save(self, *args, **kwargs):
    if self.is_new():
      self.published_at = timezone.now()
    return super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('ads:show', args=(self.id,))

  def is_author(self, user):
    return user.id == self.author.id

  def is_new(self):
    return self.id is None
