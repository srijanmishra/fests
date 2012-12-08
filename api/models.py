from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('Event', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class EventSection(models.Model):
    label = models.CharField(max_length=50)
    content = models.TextField()
    event = models.ForeignKey('Event')
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '%s - %s' % (self.event, self.label)


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class PageSection(models.Model):
    label = models.CharField(max_length=50)
    content = models.TextField()
    page = models.ForeignKey('Page')
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '%s - %s' % (self.page, self.label)
