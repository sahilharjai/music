from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	CreateAPIView,
	)
from tracks.models import Track

from .serializers import (
	TrackSerializer,
	TrackDetailSerializer,
	TrackCreateSerializer,
	TrackUpdateSerializer
	)

class TrackListView(ListAPIView):
	queryset=Track.objects.all();
	serializer_class=TrackSerializer


class TrackDetailView(RetrieveAPIView):
	queryset=Track.objects.all()
	serializer_class=TrackDetailSerializer

class TrackUpdateView(UpdateAPIView):
	queryset=Track.objects.all()
	serializer_class=TrackUpdateSerializer

class TrackCreateView(CreateAPIView):
	queryset=Track.objects.all()
	serializer_class=TrackCreateSerializer
