from django.contrib import admin

from reviews.models import Comment, Review


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'review',
        'text',
    )
    search_fields = ('review',)
    list_filter = ('review',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'score',
        'pub_date',
    )
    search_fields = ('pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
