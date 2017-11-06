from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
    url(r'^detail/(?P<id>\+)/(?P<slug>[-\w]+)/$',
    views.image_detail, name='detail'),
]
