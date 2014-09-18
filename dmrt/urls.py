from django.conf.urls import patterns, url

from .views import generate

urlpatterns = patterns('',
    url(r'^(?P<size>\d+)/(?P<image>.+)$', generate),
)
