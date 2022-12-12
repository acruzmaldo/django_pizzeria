from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': 'Customer Comment'}

        widgets = {'comment': forms.Textarea(attrs={'cols':80})}