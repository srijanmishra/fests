from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api.apihandler import EventResource, PageResource
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(EventResource())
v1_api.register(PageResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    # url(r'^fests/', include('fests.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
