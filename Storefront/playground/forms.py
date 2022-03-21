from django.contrib.auth.models import User
from django import forms
from .models import Credentials, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostUser(forms.ModelForm):
    class Meta:
        fields = ('username','password','email','first_name','last_name')
        model = User

class PostCredentials(forms.ModelForm):
    class Meta:
        fields = ('email', 'password')
        model = Credentials
