from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PkConverter, 'pk_type')

urlpatterns = [
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
    re_path(r'^re/(0*[1-9][0-9]*)/$', views.item_re_detail),
    path('converter/<pk_type:pk>/', views.item_re_detail),
]
