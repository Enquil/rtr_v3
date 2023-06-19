from newssite.models import Post
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['category'].required = True

    class Meta:

        model = Post

        fields = (
            'title', 'category',
            'featured_image',
            'excerpt', 'content',
        )

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'style': 'width: 360px; max-width: 90%;',
                    'class': 'mb-2',
                }),

            'content': SummernoteWidget(
                attrs={
                    'summernote': {
                        'width': '100%',
                        'height': '400px'
                    }
                }),

            'excerpt': forms.Textarea(
                attrs={
                    'cols': 55, 'rows': 6,
                    'class': 'mb-2',
                }),

            'featured_image': forms.FileInput(
                attrs={
                    'style': 'width: 189px;',
                    'class': 'mb-3',
                }),

            'category': forms.Select(
                attrs={
                    'style': 'width: 189px; height: 30px',
                    'class': 'mb-3',
                }),
        }

        labels = {
            'title': 'Choose your Title',
            'featured_image': 'Select an image',
        }
