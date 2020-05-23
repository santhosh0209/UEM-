from django.contrib import admin
from .models import Event, Participation


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'Department', 'event_status')



admin.site.register(Event, EventAdmin)
# admin.site.register(Participation)
