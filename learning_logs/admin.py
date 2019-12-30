from django.contrib import admin

# Importing our own class here.
from learning_logs.models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
