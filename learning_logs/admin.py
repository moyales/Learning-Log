from django.contrib import admin

# Importing our own class here.
from learning_logs.models import Topic

# Register your models here.
admin.site.register(Topic)
