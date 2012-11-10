from django.db import models
from django.template.defaultfilters import slugify


class Event(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('Event', null=True, blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]

        return super(Event, self).save(*args, **kwargs)


class Section(models.Model):
    label = models.CharField(max_length=50)
    content = models.TextField()
    event = models.ForeignKey('Event')

    def __unicode__(self):
        return '%s - %s' % (self.event, self.label)
