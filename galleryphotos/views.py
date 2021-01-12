from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location
from django import forms

# Create your views here.
def home(request):
    galleryImages = Image.objects.all()
    return  render(request, 'all/photos.html', {'galleryImages':galleryImages})

def about(request):
    return  render(request, 'about.html') 

def search_results(request):
    '''
    Method to search by category
    '''
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html', {"message":message, "images":searched_images})

    elif 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_location(category)
        message = f"{category}"
        return render(request, 'all/search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all/search.html', {"message":message}) 

def view_image(request):
    '''
    Method to get image 
    '''
    # try:
    #     image = Picture.objects.get(id =  image_id)
    # except DoesNotExist:
    #     raise Http404()
    # return render(request, "upload.html", {"image":image})
    galleryImages=Image.objects.all()
    return render(request,"photos.html", {'galleryImages':galleryImages})



