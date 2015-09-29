from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

import pages.urls
import users.urls
import ads.urls
import categories.urls
import locations.urls


urlpatterns = [
  url(r'^', include(pages.urls, namespace='pages')),
  url(r'^', include(users.urls, namespace='users')),
  url(r'^', include(ads.urls, namespace='ads')),
  url(r'^', include(categories.urls, namespace='categories')),
  url(r'^', include(locations.urls, namespace='locations')),
  url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
