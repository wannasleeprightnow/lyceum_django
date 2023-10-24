from django.contrib import admin
from django.urls import include, path

from lyceum import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include('debug_toolbar.urls')),
    )
