from django.contrib import admin

# Register your models here.
from .models import Genre

# Register your models here.
@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
	list_display=["genre_name"]
	class Meta:
		model=Genre
		list_display=['genre_name']
