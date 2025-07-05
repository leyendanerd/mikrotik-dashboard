from django.contrib import admin

from .models import MikrotikDevice


@admin.register(MikrotikDevice)
class MikrotikDeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "ip_address", "username")
