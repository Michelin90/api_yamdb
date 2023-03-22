from django.contrib import admin
from reviews.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')


admin.site.register(User, UserAdmin)
