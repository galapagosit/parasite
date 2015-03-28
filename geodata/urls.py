from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'geodata.views.checkin', name='checkin'),
)
