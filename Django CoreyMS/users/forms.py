from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # specify the model that we want this form to interact with
        fields = ['username', 'email', 'password1', 'password2'] # fields to be shown in this form


# Model form - allows us to create a form that works with a specific database model
# These forms will look like 1 form in a template

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User # specify the model that we want this form to interact with
        fields = ['username', 'email', ] # fields to be shown in this form

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']