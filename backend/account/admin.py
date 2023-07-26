from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Персональная информация', {"fields": ("full_name", "email", 'external',
            "is_active", "is_admin", "is_superuser")}),
        ('Последняя активность', {"fields": ("last_login", )}),
        ('Группы', {"fields": ("groups", )}),
        ('Права доступа', {"fields": ("user_permissions", )}),
        ('Регистрация', {"fields": ('date_create', )}),
    )
    readonly_fields = ('last_login', 'date_create')
    list_display = ("email", "full_name", 'is_active', "is_admin")
    list_filter = ("is_admin", "is_superuser", "is_active", "groups")
    search_fields = ("full_name", "email")
    ordering = ("full_name", )
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'full_name',
                'is_superuser',
                'user_permissions',
            }

        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
