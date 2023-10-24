import django.urls

from . import converters, views

django.urls.register_converter(converters.PkConverter, 'pk_type')

urlpatterns = [
    django.urls.path('', views.item_list),
    django.urls.path('<int:pk>/', views.item_detail),
    django.urls.re_path(r'^re/(0*[1-9][0-9]*)/$', views.item_re_detail),
    django.urls.path('converter/<pk_type:pk>/', views.item_re_detail),
]
