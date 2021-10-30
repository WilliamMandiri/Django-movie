from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.core import serializers


from .models import MovieModel
from .forms import MovieForm

def index(request):
    movie_list = MovieModel.objects.all()
    output = serializers.serialize('json', movie_list)
    return HttpResponse(output, content_type='application/json')

def retrieve(request, id):
    movie= MovieModel.objects.all().filter(id=id)
    output = serializers.serialize('json', movie)
    return HttpResponse(output, content_type='application/json')

def create(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MovieForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect back to home page
            return redirect('/movie')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MovieForm()

    return render(request, 'create_movie.html', {'form': form})

def delete(request, pk):
    movie = MovieModel.objects.get(id=pk)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('/movie')
    
    context = {'item': movie}
    return render(request, 'delete_movie.html', context)

def update(request, pk):
    movie = MovieModel.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movie')
    
    return render(request, 'update_movie.html', {'form': form})

