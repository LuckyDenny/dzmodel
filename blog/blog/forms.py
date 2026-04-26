from django import forms
from .models import Post, Comment, Subscribe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user', 'slug')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)