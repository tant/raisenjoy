from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *  # We need all models available 

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = ['name','date','info']

class RacerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Racer
        fields = ['name','avatar','info']


# Test bet serializer
class Bet1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bet
        fields = ['player','content']

# default bet
class BetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bet
        fields = ['player','opponent','content','race', 'racer1', 'racer2', 'status']
