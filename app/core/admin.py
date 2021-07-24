from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (
            None, {'fields': ('email', 'password')}),
        (
            _('Peronsal info'), {'fields':('name',)}),
        (
            _('Permission'),
            {
                'fields': ('is_active', 'is_superuser','is_staff')
            }
        ),
        (_('Important dates'),{'fields': ('last_login',)} )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
        ),
        )

admin.site.register(models.User, UserAdmin)
