from django.urls import path, re_path
from django.urls import include
from .views import *

app_name = 'Main'
urlpatterns = [
    path('', view_index, name='index'),
    re_path(r'^topics/$', get_all_topics, name='topics'),
    re_path(r'topics/(?P<topic_id>\d+)/$', view_detail_topic, name='topic'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', get_topic, name='topic'),
    re_path(r'^create_topic/$', create_topic, name='new_topic')

]
