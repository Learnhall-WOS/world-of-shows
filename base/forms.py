from django.forms import ModelForm
from .models import Show
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class RoleChoiceForm(UserCreationForm):
    role_choices = [('T', 'Theater'), ('A', 'Talent'), ('O', 'Other')]
    role = forms.ChoiceField(choices=role_choices, label='Role')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class ShowForm(ModelForm):
    class Meta:
        '''
            metadata
        '''
        model = Show
        fields = '__all__'
