from django.shortcuts import render

from .models import Topic
# Create your views here.


def view_index(requests):
    return render(requests, 'index.html')


def get_all_topics(requests):
    """выводим список тем"""
    topics = Topic.objects.order_by('data_added')

    return render(requests, 'topics.html', context={'topics': topics})


def view_detail_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('data_added')
    return render(request, 'topic.html', context={'topic': topic, 'entries': entries})