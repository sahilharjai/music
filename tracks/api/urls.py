from django.conf.urls import include, url
from .views import TrackListView,TrackDetailView,TrackUpdateView,TrackCreateView

urlpatterns = [
    url(r'^$', TrackListView.as_view(),name='list-api-track'),
    url(r'^(?P<pk>\d+)/$',TrackDetailView.as_view(),name='detail-api-track'),
    url(r'^(?P<pk>\d+)/edit/$',TrackUpdateView.as_view(),name='update-api-track'),
    url(r'^create/$',TrackCreateView.as_view(),name='create-api-track')
]