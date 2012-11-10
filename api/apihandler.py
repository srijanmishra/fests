from tastypie import fields
from tastypie.resources import ModelResource
from api.models import Section, Event


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'


class SectionResource(ModelResource):
    event = fields.ForeignKey(EventResource, 'event')
    
    class Meta:
        queryset = Section.objects.all()
        resource_name = 'section'
