from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    '''The home page for Learning Log.'''
    return render(request, 'learning_logs/index.html')

# The topics() function needs to get some data from the database to send to the template.
@login_required
def topics(request):
    '''Show all topics.'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # context is a dictionary in which keys are names to send to the template.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# topic() functiin needs to get the tipc and all its associated entries from database.
# UPDATE: Make sure nobody can just type the url to a certain page
@login_required
def topic(request, topic_id):
    '''Show a single topic and all its entries.'''
    topic = Topic.objects.get(id=topic_id)
    # Make sure the opic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

# newtopic() function handles two situations:
# Initial requests for the new_topic page and the processing and any data submitted in the form.
# It then needs to redirect the user back to the topics page.
@login_required
def new_topic(request):
    '''Add a new topic.'''
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# new_entry() is much like the new_topic() function:
@login_required
def new_entry(request, topic_id):
    '''Adds a new entry for a particular topic.'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# edit_entry() will return a form for editing the entry after receiving a GET request.
# When the page recieves a POST request with revised text, it will be saved to the database.
@login_required
def edit_entry(request, entry_id):
    '''Edit an existing entry.'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; prefill form with current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# check_topic_owner, (Ex. 19.3) will be a function called to verify topic owner.
def check_topic_owner(x, request):
    '''Refactored check for user verification'''
    if x != request.user:
        raise Http404