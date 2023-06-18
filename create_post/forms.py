from newssite.models import Post
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['category'].required = True

    class Meta:

        model = Post

        fields = (
            'title', 'category', 'excerpt',
            'content', 'featured_image',
        )

        widgets = {

            'content': SummernoteWidget(
                       attrs={'summernote': {
                                'width': '100%',
                                'height': '400px'
                                }}),

            'excerpt': forms.Textarea(attrs={
                                        'cols': 55, 'rows': 6,
                                        'class': 'mb-2'
                                        }),

            'featured_image': forms.FileInput(
                                    attrs={
                                        'style': 'width: 189px;',
                                        'class': 'mb-2'
                                        }),

            'category': forms.Select(
                                    attrs={
                                        'style': 'width: 189px;',
                                        'class': 'mb-2'
                                        }),
        }

        labels = {
            'featured_image': 'Select an image'
        }
