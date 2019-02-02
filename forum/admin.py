from django.contrib import admin
from .models import Section
from .models import Topic
from .models import Message

# Register your models here.
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Message)