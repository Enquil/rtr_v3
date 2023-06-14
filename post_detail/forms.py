from newssite.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Leave a comment'}
        widgets = {'body': forms.Textarea(attrs={'cols': 60, 'rows': 4})}
