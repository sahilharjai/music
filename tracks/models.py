from django.db import models
from genres.models import Genre

# Create your models here.
rating = (('1', 'Very Bad'),('2', 'Bad'),('3', 'Average'),('4', 'Good'),('5', 'Very Good'),)
    
class Track(models.Model):
	title=models.CharField(max_length=100)
	genres = models.ForeignKey(Genre)
	rating_of_track = models.CharField(
        max_length=1,
        choices=rating,
        default='3',
    )
	def get_absolute_url(self):
		return reverse("detail",kwargs={"id":self.id})
