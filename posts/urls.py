from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home),
    url(r'^create/$', views.posts_create),
    url(r'^update/$', views.posts_update),
    url(r'^detail/$', views.posts_detail),
    url(r'^delete/$', views.posts_delete),
    url(r'^', views.posts_home),
]
