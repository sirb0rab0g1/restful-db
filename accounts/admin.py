from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from .filters.admin import RegistrationStatusListFilter

# Register your models here.

from .models import (
    Information,
)


class UserProfileInline(admin.StackedInline):
    model = Information
    verbose_name_plural = 'profile'


class CustomUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]
    list_display = [
        'username',
        'email',
        'last_login',
    ]

    list_filter = [
        # RegistrationStatusListFilter,
        'last_login',
    ]


@admin.register(Information)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        # 'profile_type',
    ]
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name',
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# admin.site.register(Country)

# admin.site.site_title = 'TrivTrak Admin'
# admin.site.site_header = 'TrivTrak Admin'
