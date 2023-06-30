from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
import random


STATUS = ((0, 'Draft'), (1, 'Published'), (2, 'Disabled'))


# Sourced from Code Institute
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    friendly_name = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        '''
        Save method auto-generates the 'programatic' category name
        Example:
        - Art and Entertainment turns into programatic: art_entertainment
        '''

        # Sets category.name to none
        self.name = None
        # turns all words lowercase in friendly_name and split to list
        lower_name_list = self.friendly_name.lower().split()
        # Makes new list without 'and', if friendly_name contained any
        clean_list = [
            x for x in lower_name_list if x != 'and'
        ]
        # Join the words in clean_list with a '_'
        self.name = '_'.join(clean_list)
        return super().save(*args, **kwargs)


class Post(models.Model):
    '''
    Basic post class sourced from CodeInstitute with minor modifications:
    - extended slug that is set blank to allow title to match other posts
    - "status" is 1: "Published", as default
    '''

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    is_edited = models.BooleanField(default=False)
    excerpt = models.TextField(max_length=300, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        max_length=30,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # saves and slugifies the post after user submits the form,
    # Use random int and username to allow duplicate titles instead
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = (
                slugify(
                    self.title +
                    '-' + str(self.author.username) + str(self.author.id))
            )

        return super().save(*args, **kwargs)


class Comment(models.Model):
    '''
    Basic comment class sourced from CodeInstitute with minor modifications:
    - Parents and children to be able to use comments as a "conversation"
    - "Approved" field is set to True by default
    - Added like functionality
    '''

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.CharField(max_length=80)
    body = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    likes = models.ManyToManyField(
        User,
        related_name='comment_likes',
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    class Meta:
        ordering = ['-created_on']

    @property
    def children(self):
        '''
        Returns list of comment children, if any exists
        '''
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_top_level(self):
        '''
        Returns True if comment does not have a parent
        '''
        if self.parent is None:
            return True
        return False

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
