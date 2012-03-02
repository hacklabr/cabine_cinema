from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings
MEDIA_ROOT = settings.MEDIA_ROOT

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'menu.views.index', name='index'),
    url(r'^enqueue/(?P<clip_id>\d+)/?$', 'menu.views.enqueue'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),

)
