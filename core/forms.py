from django.forms import ModelForm
from .models import Comment, Post

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = '__all__'
        exclude = ['author']