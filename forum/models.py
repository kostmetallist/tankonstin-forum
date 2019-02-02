from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Section(models.Model):

    title = models.CharField(max_length=64)


class Topic(models.Model):

    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_anchored = models.BooleanField()

    def get_absolute_url(self): 
        return reverse('topic-detail', kwargs={'pk': self.pk})


class Message(models.Model): 

    text = models.CharField(max_length=4096)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
