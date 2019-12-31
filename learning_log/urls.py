"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# The first two lines import the functions and modules that manage URLs for
# the project and admin site.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the urls we'll write for the users app:
    path('users/', include('users.urls')),
    # Added a line to include module learning_logs.urls
    path('', include('learning_logs.urls')),
]
