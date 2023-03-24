from django.contrib import admin
from reviews.models import User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'review',
        'text',
        'created',
    )
    search_fields = ('review',)
    list_filter = ('review',)
    empty_value_display = '-пусто-'
