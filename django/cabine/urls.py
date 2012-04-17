from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings
MEDIA_ROOT = settings.MEDIA_ROOT

admin.autodiscover()

# TODO: remover urls obsoletas
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'menu.views.index', name='index'),
    url(r'^clips/(?P<order>.*)/?$', 'menu.views.clips'),
    url(r'^enqueue/(?P<clip_id>\d+)/?$', 'menu.views.enqueue'),
    url(r'^genre/(?P<genre_id>.*)/?$', 'menu.views.genre'),
    url(r'^year/(?P<year_id>.*)/?$', 'menu.views.year'),
    url(r'^director/(?P<director_id>.*)/?$', 'menu.views.director'),
    url(r'^star/(?P<star_id>.*)/?$', 'menu.views.star'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
)
