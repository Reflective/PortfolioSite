from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
# I am not sure if forms work for media but I may need to delete this file if not
class PostPictureForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["postMedia"]