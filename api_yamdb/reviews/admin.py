from django.contrib import admin
from .models import Comment


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
