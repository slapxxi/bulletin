from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'^locations/$', views.index, name='index'),
  url(r'^location/([a-zA-Z\-]+)/ads$', views.ads, name='ads'),
]
