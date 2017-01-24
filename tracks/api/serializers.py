from rest_framework import serializers

from tracks.models import Track 


class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model=Track
		fields=[
		'id',
		'title',
		]
class TrackUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Track
		fields=[
		'title',
		'rating_of_track',
		]

class TrackDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Track
		fields=[
		'id',
		'title',
		'genres',
		'rating_of_track',
		]

class TrackCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Track
		fields=[
		'title',
		'genres',
		'rating_of_track',
		]

		
		
