from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'confirmation_code',
    )
    search_fields = ('username',)
    list_filter = ('role',)
    empty_value_display = '-пусто-'
