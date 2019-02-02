from django.contrib import admin
from .models import Section, Topic, Message, UserExtra

# Register your models here.
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(UserExtra)