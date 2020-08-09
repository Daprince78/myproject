from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):  # we use this class name to link the form to the template that will render it

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
