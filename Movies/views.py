from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(movie_type='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(movie_type='comedy')
    serializer_class = MovieSerializer
