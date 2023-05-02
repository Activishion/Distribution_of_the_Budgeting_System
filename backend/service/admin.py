from django.contrib.admin import ModelAdmin, register

from .models import Message, Reporting, News


@register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('subject', 'message', "date", "author", 'PAO', 'DZO')
    list_filter = ('date', "PAO", "DZO")
    ordering = ("date", )


@register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("user", 'subscription')
    list_filter = ("subscription", )


@register(Reporting)
class ReportingAdmin(ModelAdmin):
    list_display = ("user", "report", 'data', 'subscription')
    list_filter = ("report", "subscription")
    ordering = ("user", )
