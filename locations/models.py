from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_path(self):
        return reverse('locations:ads', args=[self.slug])
