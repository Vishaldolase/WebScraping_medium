from django.urls import re_path
from . import views

app_name = 'medium'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^search/$', views.search, name = 'search'),
    re_path(r'^other_page/$', views.other_page, name = 'other_page'),
    re_path(r'^crawl_details/$', views.crawl_details, name = 'crawl_details'),
    re_path(r'^show_history/$', views.show_history, name = 'show_history'),


]
