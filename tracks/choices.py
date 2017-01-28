rating = (('1', 'Very Bad'),('2', 'Bad'),('3', 'Average'),('4', 'Good'),('5', 'Very Good'),)

from django.forms import ModelChoiceField

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return  obj.genre_name