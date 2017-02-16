from django.contrib import admin

from .models import Sound

class SoundAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sound, SoundAdmin)
