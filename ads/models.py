from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.urlresolvers import reverse

from djmoney.models.fields import MoneyField

from users.models import User


class Ad(models.Model):
  title        = models.CharField(max_length=120)
  description  = models.TextField(validators=[MinLengthValidator(60),])
  author       = models.ForeignKey(User)
  image        = models.ImageField(upload_to='img', blank=True)
  published_at = models.DateTimeField(auto_now=True)
  price        = MoneyField(max_digits=10, decimal_places=2,
                 default_currency='RUB', validators=[MinValueValidator(0.01)])

  def get_absolute_url(self):
    return reverse('ads:show', args=(self.id,))
