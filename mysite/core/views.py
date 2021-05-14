from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all();
    serializer_class = GroupSerializer

class BetViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all();
    serializer_class = BetSerializer
