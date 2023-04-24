from django.contrib.admin import ModelAdmin, register

from .models import Message, Reporting, News


@register(Message)
class MessageAdmin(ModelAdmin):
    fields = []


@register(News)
class NewsAdmin(ModelAdmin):
    pass


@register(Reporting)
class ReportingAdmin(ModelAdmin):
    pass
