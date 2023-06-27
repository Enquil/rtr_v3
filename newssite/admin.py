from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'author')

    list_display = (
        'author',
        'title',
        'slug',
        'status',
        'created_on',
        'category'
    )

    search_fields = ('title', 'content')
    summernote_fields = ('content')
    actions = [
        'disable_selected_posts',
        'publish_selected_posts'
    ]

    def disable_selected_posts(self, request, queryset):
        queryset.update(status=2)

    def publish_selected_posts(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'author',
        'id',
        'body',
        'post',
        'created_on',
        'approved',
        'parent_id',
    )

    list_filter = ('approved', 'author')
    search_fields = ('author', 'email', 'body')
    actions = [
        'approve_selected_comments',
        'disable_selected_comments'
    ]

    # Sets approved to False and prevents comment from showing in post
    def disable_selected_comments(self, request, queryset):
        queryset.update(approved=False)

    # Sets approved to True
    def approve_selected_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'friendly_name', 'name')
