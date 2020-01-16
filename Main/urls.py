from django.urls import path, re_path
from django.urls import include
from .views import *

app_name = 'Main'
urlpatterns = [
    path('', view_index, name='index'),
    re_path(r'^topics/$', get_all_topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', get_topic, name='topic'),
    re_path(r'^create_topic/$', create_topic, name='new_topic'),
    re_path(r'^create_entry/(?P<topic_id>\d+)/$', create_entry, name='create_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', edit_entry, name='edit_entry'),


]
