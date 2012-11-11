from django.contrib import admin
from api.models import Event, EventSection, Page, PageSection


class EventSectionInline(admin.StackedInline):
    model = EventSection
    extra = 3


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    inlines = [EventSectionInline]


class PageSectionInline(admin.StackedInline):
    model = PageSection
    extra = 3


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    inlines = [PageSectionInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
