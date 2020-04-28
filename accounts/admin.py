from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'email', 'phone', 'birth_date', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'phone', 'birth_date', 'last_login')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    list_display = ['username', 'name', 'email', 'phone', 'birth_date', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserAdmin)
