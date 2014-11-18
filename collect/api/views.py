import json
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

from collect.api.serializers import UserSerializer, CategorySerializer, PlaceSerializer

from collect.models import User, Place, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    search_fields = ('city', 'country', 'owner')
    permission_classes = (AllowAny,)
