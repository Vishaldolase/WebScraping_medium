from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^medium/', include('medium.urls')),
    re_path(r'^', include('medium.urls')),
]