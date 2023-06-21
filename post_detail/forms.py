from newssite.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ('body',)
        labels = {'body': ''}

        widgets = {

            'body': forms.Textarea(attrs={
                    'class': 'w-100 h-100',
                    'cols': 80,
                    'rows': 5,
                    'placeholder': 'Leave a Comment..',
                })
        }
