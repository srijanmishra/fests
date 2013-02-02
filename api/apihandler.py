from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from api.models import Event, EventSection, Page, PageSection


class EventResource(ModelResource):
    parent = fields.ToOneField('self', 'parent', null=True)
    sections = fields.ToManyField('api.apihandler.EventSectionResource',
        'eventsection_set', full=True, null=True)


    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']
        filtering = {
            'parent': ALL_WITH_RELATIONS,
            'slug': ('exact'),
        }


class EventSectionResource(ModelResource):
    class Meta:
        queryset = EventSection.objects.all()
        resource_name = 'eventsection'
        allowed_methods = ['get']
        fields = ['label', 'content', 'order']
        include_resource_uri = False


class PageResource(ModelResource):
    sections = fields.ToManyField('api.apihandler.PageSectionResource',
        'pagesection_set', full=True, null=True)


    class Meta:
        queryset = Page.objects.all()
        resource_name = 'page'
        allowed_methods = ['get']
        filtering = {
            'slug': ('exact'),
        }


class PageSectionResource(ModelResource):
    class Meta:
        queryset = PageSection.objects.all()
        resource_name = 'pagesection'
        allowed_methods = ['get']
        fields = ['label', 'content', 'order']
        include_resource_uri = False


