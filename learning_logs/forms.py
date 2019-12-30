from django import forms

from .models import Topic

# This is the simplest way to build a from in Django.
# Using ModelForm, which uses information from models we defined previously

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        # Don't generate a label for the text field.
        labels = {'text': ''}