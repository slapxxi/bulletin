from django.conf.urls import include, url
from django.contrib import admin

import pages.urls
import users.urls

urlpatterns = [
  url(r'^', include(pages.urls, namespace='pages')),
  url(r'^', include(users.urls, namespace='users')),
  url(r'^admin/', include(admin.site.urls)),
]
