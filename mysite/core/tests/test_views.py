import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import *
from ..serializers import *


# initialize the APIClient app
client = Client()