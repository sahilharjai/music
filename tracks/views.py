from django.shortcuts import render,get_object_or_404,redirect
from .models import Track
from genres.models import Genre
from .forms import TrackForm,TrackUpdateForm
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.

def track_list(request):
	track_list=Track.objects.all();
	paginator = Paginator(track_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		track = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		track = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		track = paginator.page(paginator.num_pages)



	context={
		"track_list":track,
	}
	return render(request,'track_list.html',context)



    


    
@require_http_methods(['GET','POST'])
def track_create(request):
	if request.method=='GET':
		form=TrackForm()
		return render(request,'track_add.html',{'form':form})
	else:
		form=TrackForm(request.POST)		
		if form.is_valid():
			title=form.cleaned_data['title']
			gene=form.cleaned_data['genre']
			track_obj=Track(title=title)
			obj=Genre.objects.filter(genre_name=gene)
			if not obj:
				
				obj=Genre.objects.create(genre_name=gene)
				obj.save(force_insert=True)
				track_obj.genres=obj
			else:
				track_obj.genres=obj[0]


			
			track_obj.save()
			return redirect(reverse('list'))
		else:
			return render(request,'track_add.html',{'form':form})


@require_http_methods(['GET','POST'])
def track_update(request,id=None):
	track_obj=get_object_or_404(Track,id=id)
	obj={"title":track_obj.title,"genre":track_obj.genres.genre_name}
	if request.method=='GET':
		form=TrackUpdateForm()
	else:
		form=TrackUpdateForm(request.POST)
		if form.is_valid():
			track_obj=form.save()
			return redirect(reverse('list'))
	context = { 'form' : form }
	return render(request, 'track_form.html', context)

	

def track_detail(request,id=None):
	instance=get_object_or_404(Track,id=id);
	context={
		"title":instance.title,
		"instance":instance,
		"id":instance.id
	}
	return render(request,'track_detail.html',context)

