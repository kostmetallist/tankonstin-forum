from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic.list import MultipleObjectMixin
from django.contrib import messages
from .models import Message, Topic, Section
from .forms import UserRegistrationForm, MessageCreationForm


def forumHome(request):

    context = {
        'recent_topics': Topic.objects.all().order_by('-id')[:4],
    }

    return render(request, 'forum/home.html', context)

def userRegistration(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account for {username}!')
            return redirect('forum-home')

    # 'GET' usually
    else:
        form = UserRegistrationForm()

    return render(request, 'forum/user-registration.html', {'form': form})


class ForumUserDetailView(DetailView):

    # w/o setting this, header shows incorrect user as logged in
    context_object_name = 'profile_owner'
    model = User
    template_name = 'forum/user-detail.html'


class TopicDetailView(DetailView, MultipleObjectMixin):

    model = Topic
    template_name = 'forum/topic-detail.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):

        #context = super().get_context_data(**kwargs)
        #context['topic_messages'] = Message.objects.all().filter(topic_id=self.kwargs['pk']).order_by('timestamp')
        object_list = Message.objects.all().filter(topic_id=self.kwargs['pk']).order_by('timestamp')
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class MessageCreateView(LoginRequiredMixin, CreateView):

    model = Message
    template_name = 'forum/message-create-form.html'
    # fields = ['text']
    form_class = MessageCreationForm

    def get_success_url(self):
        return reverse('topic-detail', kwargs={'pk': self.kwargs['topic']})

    def form_valid(self, form):

        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['topic'])
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Message
    template_name = 'forum/message-delete.html'

    def get_success_url(self):
        return reverse('topic-detail', kwargs={'pk': Message.objects.get(id=self.kwargs['pk']).topic_id})

    def test_func(self):

        if self.request.user == self.get_object().author:
            return True

        return False

class SectionListView(ListView):

    model = Section
    template_name = 'forum/index.html'