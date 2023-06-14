from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
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
    actions = ['disable_selected_posts', 'publish_selected_posts']

    def disable_selected_posts(self, request, queryset):
        queryset.update(status=2)

    def publish_selected_posts(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
                    'name',
                    'id',
                    'body',
                    'post',
                    'created_on',
                    'approved',
                    'parent_id',
                    )
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_selected_comments', 'disable_selected_comments']

    def disable_selected_comments(self, request, queryset):
        queryset.update(approved=False)

    def approve_selected_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'name',
                    'friendly_name',
                   )
