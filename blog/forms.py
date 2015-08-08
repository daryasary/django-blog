from django import forms
from blog.models import Comment
from datetime import datetime

class CommentForm(forms.ModelForm):
	date = forms.DateField(initial=datetime.now(), widget=forms.HiddenInput())
	post = forms.IntegerField(widget=forms.HiddenInput())
	class Meta:
		model = Comment

		widgets = {
            'name': forms.TextInput(attrs={'class':"form-control", 'id':"pwd", 'placeholder':"Enter your name"}),
            'email': forms.TextInput(attrs={'class':"form-control", 'id':"pwd", 'placeholder':"Enter your email address"}),
        	'website':forms.TextInput(attrs={'class':"form-control", 'id':"pwd", 'placeholder':"Enter your website"}),
        	'body': forms.Textarea(attrs={'class':"form-control", 'id':"pwd", 'placeholder':"Enter your comment"}),
        	}
		fields = ('name', 'email', 'website', 'body')