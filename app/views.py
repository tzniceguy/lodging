from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class ListUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListLodge(generics.ListCreateAPIView):
    queryset = Lodge.objects.all()
    serializer_class = LodgeSerializer
