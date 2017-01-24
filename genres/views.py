from django.shortcuts import render,get_object_or_404,redirect
from .models import Genre
from .forms import GenreForm
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.core.urlresolvers import reverse


# Create your views here.

def genre_list(request):
	genre_list=Genre.objects.all();
	context={
		"genre_list":genre_list,
	}
	return render(request,'genre_list.html',context)

@require_http_methods(['GET','POST'])
def genre_create(request):
	if request.method=='GET':
		form=GenreForm()
		return render(request,'genre_add.html',{'form':form})
	else:
		form=GenreForm(request.POST)		
		if form.is_valid():
			genre_obj=form.save(commit=False)
			
			genre_obj.save()
			return redirect(reverse('list-genre'))
		else:
			return render(request,'genre_add.html',{'form':form})


@require_http_methods(['GET','POST'])
def genre_update(request,id=None):
	genre_obj=get_object_or_404(Genre,id=id)
	if request.method=='GET':
		form=GenreForm(instance=genre_obj)
	else:
		form=GenreForm(request.POST,instance=genre_obj)
		if form.is_valid():
			genre_obj=form.save()
			return redirect(reverse('list-genre'))
	context = { 'form' : form }
	return render(request, 'genre_form.html', context)

	

def genre_detail(request,id=None):

	instance=get_object_or_404(Genre,id=id);
	context={
		
		"instance":instance,
	}
	return render(request,'genre_detail.html',context)

