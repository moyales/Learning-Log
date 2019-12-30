'''Defines the URL patters for learning_logs.'''
# Docsting makes it easy to tell which urls.py we're working in.

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # --Ch. 19 URLS ; Allowing User Input--
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
]