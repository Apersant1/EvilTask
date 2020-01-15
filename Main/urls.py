from django.urls import path, re_path
from django.urls import include
from .views import *

app_name = 'Main'
urlpatterns = [
    path('', view_index, name='index'),
    re_path(r'^topics/$', get_all_topics, name='topics'),
]