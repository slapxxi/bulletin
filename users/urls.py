from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
  url(r'^register/$', views.Register.as_view(), name='register'),
  url(r'^user/(\d+)/$', views.user, name='user'),
  url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
  url(r'^', include('django.contrib.auth.urls')),
]
