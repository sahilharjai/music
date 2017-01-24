from django.contrib import admin

# Register your models here.
from .models import Track

# Register your models here.
@admin.register(Track)
class TrackModelAdmin(admin.ModelAdmin):
	list_display=["title"]
	class Meta:
		model=Track
