from django import forms

from .models import Track
from genres.models import Genre

class TrackForm(forms.Form):
	title=forms.CharField(max_length=100)
	genre=forms.CharField(max_length=100)

	def clean_genre(self):
		data_genre=self.cleaned_data.get('genre','')
		if Genre.objects.filter(genre_name=data_genre).exists():
			return data_genre
		raise forms.ValidationError('This Genre Does not exist Please add a valid Genre')
		

	def clean_title(self):
		data_title=self.cleaned_data.get('title','')
		if Track.objects.filter(title=data_title).exists():
			raise forms.ValidationError('Title Already Exists')
		return data_title



class TrackUpdateForm(forms.Form):
	title=forms.CharField(max_length=100)
	genre=forms.CharField(max_length=100)
	

	def clean_genre(self):
		data_genre=self.cleaned_data.get('genre','')
		if Genre.objects.filter(genre_name=data_genre).exists():
			return data_genre
		raise forms.ValidationError('This Genre Does not exist Please add a valid Genre')
		

	def clean_title(self):
		data_title=self.cleaned_data.get('title','')
		if Track.objects.filter(title=data_title).exists():
			raise forms.ValidationError('Title Already Exists')
		return data_title
	
	
		