from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer   


class HotTourViewSet(viewsets.ModelViewSet):
    queryset = HotTour.objects.all()
    serializer_class = HotTourSerializer

class ZayavkaViewSet(viewsets.ModelViewSet):
    queryset = Zayavka.objects.all()
    serializer_class = ZayavkaSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class OtzyvViewSet(viewsets.ModelViewSet):
    queryset = Otzyv.objects.all()
    serializer_class = OtzyvSerializer

class CaruselViewSet(viewsets.ModelViewSet):
    queryset = Carusel.objects.all()
    serializer_class = CaruselSerializer



def main(request):
    hot_tours = Tours.objects.all()
    context = {'hottours':hot_tours}
    return render(request,'tour/index.html', context)

def tours(request):
    context = {}
    return render(request,"tour/tours.html", context)

def tour_detail(request):
    context = {}
    return render(request,'tour/tour-detail.html', context)

def about_us(request):
    context = {}
    return render(request,'tour/about-us.html', context)

def photos(request):
    context = {}
    return render(request,'tour/photos.html', context)