from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'^ads/$', views.index, name='index'),
  url(r'^ads/categories/$', views.categories, name='categories'),
  url(r'^ads/locations/$', views.locations, name='locations'),
]
