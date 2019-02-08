from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message, UserExtra


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MessageCreationForm(forms.ModelForm):
    class Meta:

        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea()
        }


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'email', 
            'first_name', 'last_name']


class UserExtraUpdateForm(forms.ModelForm):

    description = forms.Textarea()

    class Meta:

        model = UserExtra
        fields = ['description', 'avatar']
        widgets = {
            'description': forms.Textarea()
        }