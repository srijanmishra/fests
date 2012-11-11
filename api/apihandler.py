from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from api.models import Section, Event


class EventResource(ModelResource):
    parent = fields.ToOneField('self', 'parent', null=True)
    sections = fields.ToManyField('api.apihandler.SectionResource',
        'section_set', full=True, null=True)
    
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']
        filtering = {
            'parent': ALL_WITH_RELATIONS,
            'slug': ('exact'),
        }


class SectionResource(ModelResource):
    class Meta:
        queryset = Section.objects.all()
        resource_name = 'section'
        allowed_methods = ['get']
        fields = ['label', 'content', 'order']
        include_resource_uri = False
        ordering = ['-order']
