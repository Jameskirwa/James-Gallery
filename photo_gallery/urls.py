from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import os
from photos.views import photo_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
