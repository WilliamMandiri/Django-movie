from django.forms import ModelForm
from .models import MovieModel

class MovieForm(ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'