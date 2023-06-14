from newssite.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ('body',)
        labels = {'body': ''}

        widgets = {

            'body': forms.Textarea(attrs={

                    'cols': 80,
                    'rows': 4,
                    'placeholder': 'Leave a Comment..',
                })
        }
