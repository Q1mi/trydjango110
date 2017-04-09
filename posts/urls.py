from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home, name="list"),
    url(r'^create/$', views.posts_create, name="create"),
    url(r'^(?P<id>\d+)/update/$', views.posts_update, name="update"),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$', views.posts_delete, name="delete"),
    url(r'', views.posts_home),
]
