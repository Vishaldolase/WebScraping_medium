from django.conf.urls import include,url
from django.urls import re_path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^medium/', include('medium.urls')),
    re_path(r'^', include('medium.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]