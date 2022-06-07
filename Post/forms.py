from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...',
            'class': 'md-textarea form-control'
            }))

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '1',
                   'placeholder': 'Add a Comment...',
                   'class': 'md-textarea form-control'
                }
        ))

    class Meta:
        model = Comment
        fields = ['comment']
