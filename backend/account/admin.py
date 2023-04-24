from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Персональная информация', {"fields": ("name", "email", "is_active",
                    "is_admin", "is_superuser")}),
        ('Группы', {"fields": ("groups", )}),
        ('Права доступа', {"fields": ("user_permissions", )})
    )
    list_display = ("email", "name", 'is_active', "is_admin")
    list_filter = ("is_admin", "is_superuser", "is_active", "groups")
    search_fields = ("name", "email")
    ordering = ("name", )
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
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
