from django.contrib.admin import ModelAdmin, register

from .models import Message, Reporting


@register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('subject', 'message', "date", "author", 'PAO', 'DZO')
    list_filter = ('date', "PAO", "DZO")
    ordering = ("-date", )


@register(Reporting)
class ReportingAdmin(ModelAdmin):
    list_display = ("user", "report", 'full_name', 'data', 'subscription')
    list_filter = ("report", "subscription")
    ordering = ("-data", )
    readonly_fields = ('data', )
    fieldsets = (
        ('', {"fields":("user", 'full_name', "report", 'data', 'subscription')}),
        ('Moderation', {"fields": ('added_via_portal', 'moderator_is_decision', 'moderator', 
            'data_moderation', 'comment')}),
        ('Removal', {"fields": ('date_delete', 'comment_delete')}),
    )
