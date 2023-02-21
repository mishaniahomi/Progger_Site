from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index
from django.contrib.staticfiles.views import serve as static_serve
from django.views.static import serve as media_serve


urlpatterns = [
                  path('', index, name="index"),
                  path('testforuser/', include('testforuser.urls')),
                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', static_serve,
                       {'insecure': True})),
    urlpatterns.append(path('media/<path:path>', media_serve,
                            {'document_root': settings.MEDIA_ROOT}))