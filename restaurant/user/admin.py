from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'last_active_datetime')
    list_filter = ('username',)
    search_fields = ('username', 'email',)
    list_editable = ('first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = [
        ('Personal Info', {
            'fields': [
                'username', 'email', 'first_name', 'last_name', 'password'
            ],
        }),
        ('About', {
            'fields': ['about']
        }),
        ('Permissions', {
            'fields': ['is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions']
        }),
        ('Important Dates', {
            'fields': ['last_login', 'last_active_datetime']
        }),
    ]