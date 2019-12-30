from django import forms

from .models import Topic, Entry

# This is the simplest way to build a from in Django.
# Using ModelForm, which uses information from models we defined previously
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        # Don't generate a label for the text field.
        labels = {'text': ''}

# We need to create a form associated with the Entry model,
# with a bit more customisation than TopicForm:
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # Default col size is 40.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}