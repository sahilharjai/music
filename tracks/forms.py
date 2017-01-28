from django import forms
from .choices import rating

from .models import Track
from genres.models import Genre
from .choice import vModelChoiceField

class TrackForm(forms.Form):
	title=forms.CharField(max_length=100)
	genre=vModelChoiceField(queryset=Genre.objects.all(),to_field_name="genre_name")
	rating_of_track = forms.ChoiceField(
        choices = rating, label="", initial='', widget=forms.Select(), required=True
    )

	#def clean_genre(self):
	#	data_genre=self.cleaned_data.get('genre','')
	#	if Genre.objects.filter(genre_name=data_genre).exists():
	#		return data_genre
	#	raise forms.ValidationError('This Genre Does not exist Please add a valid Genre')
		

	def clean_title(self):
		data_title=self.cleaned_data.get('title','')
		if Track.objects.filter(title=data_title).exists():
			raise forms.ValidationError('Title Already Exists')
		return data_title



class TrackUpdateForm(forms.ModelForm):
	class Meta:
		model=Track
		fields=[
		'title',
		'rating_of_track',
		]
	
	
