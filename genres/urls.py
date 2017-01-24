from django.conf.urls import include, url
from .views import genre_list,genre_create,genre_update,genre_detail


urlpatterns = [
    url(r'^$', genre_list,name='list-genre'),
    url(r'^create/$', genre_create,name='create-genre'),
    url(r'^(?P<id>\d+)/edit/', genre_update,name='update-genre'),
    #url(r'^(?P<id>\d+)/delete/', post_delete),
    url(r'^detail/(?P<id>\d+)/', genre_detail,name='detail-genre'),
]