from django.shortcuts import render, redirect
from .models import Image, Category, Location

def index(request):
  all_photos = Image.objects.all()
  all_category = Category.objects.all()
  all_location = Location.objects.all()

  if request.GET.get('location'):
    images = Image.filter_by_location(request.GET.get('location'))
    return render(request, 'galltemp/location.html', {'all_photos':images, 'all_category':all_category, 'locationn': request.GET.get('location')})

  return render(request, 'galltemp/index.html', {'all_photos':all_photos, 'all_category':all_category, 'all_location':all_location})
  
  