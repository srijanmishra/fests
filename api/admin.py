from django.contrib import admin
from api.models import Section, Event


class SectionInline(admin.StackedInline):
    model = Section
    extra = 3


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    inlines = [SectionInline]


admin.site.register(Event, EventAdmin)
