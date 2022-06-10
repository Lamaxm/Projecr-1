from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, profil_client,profil_consultant


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'as_consultant', 'as_client', 'password1', 'password2',)
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'as_consultant', 'as_client', 'password',)
        }),
    )
    list_display = ['id','email', 'username', 'as_consultant', 'as_client']
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(profil_consultant)
admin.site.register(profil_client)
admin.site.register(User, UserAdmin)