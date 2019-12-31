from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.

# logout_view() function imports the logout function and calls it to redirect back to home page.
def logout_view(request):
    '''Log the user out.'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
