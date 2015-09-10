from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='pages/index'),
  url(r'^about/$', views.about, name='pages/about'),
]
