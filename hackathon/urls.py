from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^wall/', include('wall.urls')),
)

from django.contrib import admin
admin.autodiscover()
urlpatterns += patterns('',(r'^admin/', include(admin.site.urls)))
