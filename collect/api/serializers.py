
from rest_framework import serializers
from collect.models import User, Category, Place


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

class PlaceSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    # category = CategorySerializer()

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'category', 'streetnum', 'street', 'city', 'country', 'image', 'owner', 'follower', 'latitude', 'longitude','created_time', 'status')

