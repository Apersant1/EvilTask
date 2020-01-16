from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
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

def get_topic(requests, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    return render(requests, 'topic.html', context={'topic':topic, 'entries':entries})

def create_topic(request):
    print(request)
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Main:topics'))
    return render(request, 'new_topic.html', context={'form':form})
