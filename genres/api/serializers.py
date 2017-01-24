from rest_framework import serializers

from genres.models import Genre 


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=Genre
		fields=[
		'id',
		'genre_name',
		]

class GenreDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Genre
		fields=[
		'id',
		'genre_name',
		]

class GenreCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Genre
		fields=[
		'genre_name',
		]

		
		
