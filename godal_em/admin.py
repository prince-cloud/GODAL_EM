from urllib.request import Request
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "GODAL EC"
admin.site.index_title = "Welcome to GODAL EC Administration Panel"

#admin.site.register(Meter)
#admin.site.register(Request)

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    def Activate(self, request, queryset):
        queryset.update(active=True)
    Activate.short_description = "Activate"
    def Deactivate(self, request, queryset):
        queryset.update(active=False)
    Deactivate.short_description = "Dectivate"
    list_display = (
        "user",
        "meter_id",
        "current_power",
        "active",
    )
    list_filter = (
        "active",
    )
    actions = ["Activate", "Deactivate"]

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def grant(self, request, queryset):
        queryset.update(granted=True)

    grant.short_description = "Grant"
    list_display = (
        "by",
        "amount",
        "granted",
    )
    list_filter = (
        "granted",
    )
    actions = ["grant",]
