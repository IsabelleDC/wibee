import json
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

from collect.api.serializers import UserSerializer, CategorySerializer, PlaceSerializer

from collect.models import User, Place, Category

# It looks like these are not working with authentication yet? or there's a bug here and it would allow
# anyone to edit/delete anyone else's Places.

# Likewise we probably don't want GET, POST, PATCH, DELETE for each one of these models here

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    search_fields = ('city', 'country', 'owner')
