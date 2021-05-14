from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from .serializers import *

# Làm cái index cho vui 
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello. You're about to get data.")

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RaceViewset(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RacerViewset(viewsets.ModelViewSet):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer

class BetViewset(viewsets.ModelViewSet):
    queryset = Bet.objects.all();
    serializer_class = BetSerializer
