from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
from .forms import EntryForm
# Create your views here.


def view_index(requests):
    return render(requests, 'index.html')


def get_all_topics(requests):
    """выводим список тем"""
    topics = Topic.objects.order_by('data_added')

    return render(requests, 'topics.html', context={'topics': topics})



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

def create_entry(request, topic_id):
    """Добавляем запись к конкретной теме"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()   # Данные не отправлялись, создаётся пустая форма
    else:
        #Получен POST запрос
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('Main:topic', args=[topic_id]))

    return render(request, 'new_entry.html', context={'topic': topic, 'form': form})

