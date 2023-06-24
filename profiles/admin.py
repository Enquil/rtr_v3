from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    '''
        Only used this to check profiles were updating correctly
        Should be removed before production
    '''
    list_display = ('id', 'user')
