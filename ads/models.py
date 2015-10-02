from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.urlresolvers import reverse

from djmoney.models.fields import MoneyField

from users.models import User


class Ad(models.Model):
  # TODO: Add ability to add a set of images.
  title        = models.CharField(max_length=120)
  description  = models.TextField(validators=[MinLengthValidator(60),])
  author       = models.ForeignKey(User)
  image        = models.ImageField(upload_to='img', blank=True)
  published_at = models.DateTimeField()
  price        = MoneyField(max_digits=10, decimal_places=2,
                 default_currency='RUB', validators=[MinValueValidator(0.01)])

  def save(self, *args, **kwargs):
    if self.id is None:
      self.published_at = now()
    return super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('ads:show', args=(self.id,))

  def is_author(self, user):
    return user.id == self.author.id
