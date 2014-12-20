from django.contrib import admin
from .models import PushbulletClient


class PushbulletClientAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'signed_on')


admin.site.register(PushbulletClient, PushbulletClientAdmin)
