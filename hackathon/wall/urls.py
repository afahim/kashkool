from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

import os
APP_PATH = os.path.abspath(os.path.dirname(__file__))

urlpatterns = patterns('',
    (r'^$', 'wall.views.index'),
    (r'^wallReturn/(?P<tag>\w*)/(?P<pageid>\d+)/$', 'wall.views.wallReturn'),
    (r'^(?P<mediaid>\d+)/getMedia/$', 'wall.views.getMedia'),
    (r'^(?P<mediaid>\d+)/vote/$', 'wall.views.vote'),
    (r'^(?P<mediaid>\d+)/zoomBox/$', 'wall.views.zoomBox'),
    (r'^(?P<mediaid>\d+)/comment/$', 'wall.views.comment'),
    (r'^tagslist/$', 'wall.views.randomTags'),
    (r'^uploader/$', 'wall.views.uploader'),
    (r'^add/$', 'wall.views.add'),
)

# serving static files
urlpatterns += patterns('',
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(APP_PATH, 'static/css'), 'show_indexes': settings.DEBUG}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(APP_PATH, 'static/js'), 'show_indexes': settings.DEBUG}),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(APP_PATH, 'static/media'), 'show_indexes': settings.DEBUG}),
)



