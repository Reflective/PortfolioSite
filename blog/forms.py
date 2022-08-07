from django import forms
from .models import Post

#  Uses ModelForm with the Post model and included fields
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "postMedia"]
