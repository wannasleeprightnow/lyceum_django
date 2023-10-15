"""
URL configuration for lyceum project.
"""
from django.urls import include, path

from . import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
]


if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include('debug_toolbar.urls')),
    )
