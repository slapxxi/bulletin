from django.conf.urls import include, url
from django.contrib import admin

import pages.urls
import users.urls
import ads.urls


urlpatterns = [
  url(r'^', include(pages.urls, namespace='pages')),
  url(r'^', include(users.urls, namespace='users')),
  url(r'^', include(ads.urls, namespace='ads')),
  url(r'^admin/', include(admin.site.urls)),
]
