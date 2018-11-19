from __future__ import unicode_literals

from django import forms
from blog.models import Comment
from datetime import datetime


class CommentForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.now(), widget=forms.HiddenInput())
    post = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')
