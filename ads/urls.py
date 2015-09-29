from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'^ads/$', views.index, name='index'),
  url(r'^ads/new/$', views.CreateAd.as_view(), name='new'),
  url(r'^ad/(\d+)/$', views.show, name='show'),
]
