from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from django.db import models
from .models import Image


# Create your views here.
def mygallery(request):
    date = dt.date.today()
    photos = Image.get_all()
    return render(request, 'all-pics/home.html', {"date": date, "photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any Image Category"
        return render(request, 'all-pics/search.html',{"message":message})

def get_london(request):
    image_location = Image.manchester()
    return render(request, 'image_location.html', {"images": image_location})


def get_losangeles(request):
    image_location = Image.florida()
    return render(request, 'image_location.html', {"images": image_location})