from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	CreateAPIView,
	)
from .permissions import IsOwnerOrReadOnly
from genres.models import Genre

from .serializers import (
	GenreSerializer,
	GenreDetailSerializer,
	GenreCreateSerializer,
	)

class GenreListView(ListAPIView):
	queryset=Genre.objects.all();
	serializer_class=GenreSerializer


class GenreDetailView(RetrieveAPIView):
	queryset=Genre.objects.all()
	serializer_class=GenreDetailSerializer

class GenreUpdateView(RetrieveUpdateAPIView):
	queryset=Genre.objects.all()
	serializer_class=GenreSerializer

class GenreCreateView(CreateAPIView):
	queryset=Genre.objects.all()
	serializer_class=GenreCreateSerializer
