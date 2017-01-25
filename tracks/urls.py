from django.conf.urls import include, url
from .views import track_list,track_create,track_update,track_detail,search


urlpatterns = [
    url(r'^$', track_list,name='list'),
    url(r'^search/$',search,name='search-tracks'),
    url(r'^create/$', track_create,name='create'),
    url(r'^(?P<id>\d+)/edit/', track_update,name='update'),
    #url(r'^(?P<id>\d+)/delete/', post_delete),
    url(r'^detail/(?P<id>\d+)/', track_detail,name='detail'),
]