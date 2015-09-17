from django.db import models

from users.models import User

#
# class Category(models.Model):
#   name = models.CharField(max_length=120)
#   description = models.TextField()
#
#
# class Ad(models.Model):
#   author = models.ForeignKey(User)
#   category = models.ManyToManyField(Category)
#   published = models.DateTimeField()
#   location = models.LocationField()
