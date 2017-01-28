from django.forms import ModelChoiceField

class vModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return "%s" % obj.genre_name