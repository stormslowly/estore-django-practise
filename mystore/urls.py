from django.conf.urls import patterns, include, url
from django.contrib import admin
from mystore import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mystore.views.home', name='home'),
    # url(r'^mystore/', include('mystore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('catalog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root' : os.path.join(settings.CURRENT_DIR, 'media') }),
)


