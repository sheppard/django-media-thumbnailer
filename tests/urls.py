from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^generate/', include('dmt.urls'))
)
