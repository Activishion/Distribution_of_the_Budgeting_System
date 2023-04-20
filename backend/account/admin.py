# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group


# @admin.register(UserAdmin, Group)
# class UserAdmin(UserAdmin):

#     list_display = [
#         'date_of_birth',
#         'email',
#         'firstname',
#         'is_admin',
#         'lastname',
#         'middlename',
#     ]

#     list_filter = ('is_admin',)

#     fieldsets = (
#                 (None, {'fields': ('email', 'password')}),
#                 ('Personal info', {
#                  'fields': (
#                      'avatar',
#                      'date_of_birth',
#                      'firstname',
#                      'lastname',
#                      'middlename',
#                  )}),
#                 ('Permissions', {'fields': ('is_admin',)}),
#                 ('Important dates', {'fields': ('last_login',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'date_of_birth',
#                 'email',
#                 'password1',
#                 'password2'
#             )}
#         ),
#     )

#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
