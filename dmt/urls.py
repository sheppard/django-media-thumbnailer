from django.conf.urls import url

from .views import generate

urlpatterns = [
    url(r'^(?P<size>\d+)/(?P<image>.+)$', generate),
]
