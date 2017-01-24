from django.conf.urls import include, url
from .views import GenreListView,GenreDetailView,GenreUpdateView,GenreCreateView

urlpatterns = [
    url(r'^$', GenreListView.as_view(),name='list-api-genre'),
    url(r'^(?P<pk>\d+)/$',GenreDetailView.as_view(),name='detail-api-genre'),
    url(r'^(?P<pk>\d+)/edit/$',GenreUpdateView.as_view(),name='update-api-genre'),
    url(r'^create/$',GenreCreateView.as_view(),name='create-api-genre')
]