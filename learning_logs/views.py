from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    '''The home page for Learning Log.'''
    return render(request, 'learning_logs/index.html')

# The topics() function needs to get some data from the database to send to the template.
def topics(request):
    '''Show all topics.'''
    topics = Topic.objects.order_by('date_added')
    # context is a dictionary in which keys are names to send to the template.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# topic() functiin needs to get the tipc and all its associated entries from database.
def topic(request, topic_id):
    '''Show a single topic and all its entries.'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
