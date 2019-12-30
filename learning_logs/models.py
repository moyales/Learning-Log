from django.db import models

# Create your models here.

# A model tells Django how to work with the data that will be stored in the app.
# In code terms, a model is a class - with attributes and methods

class Topic(models.Model):
    '''A topic the user is learning about.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.text
