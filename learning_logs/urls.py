'''Defines the URL patters for learning_logs.'''
# Docsting makes it easy to tell which urls.py we're working in.

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]