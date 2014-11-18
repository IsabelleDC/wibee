
from rest_framework import serializers
from collect.models import User, Category, Place


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        # read_only_fields = ('date_joined',)
        # write_only_fields = ('password',)

    # def restore_object(self, attrs, instance=None):
    #     profile = super(UserSerializer, self).restore_object(
    #         attrs, instance
    #     )
    #
    #     if profile:
    #         user = profile.user
    #         # user.email = attrs.get('user.email', user.email)
    #         user.first_name = attrs.get('user.first_name', user.first_name)
    #         user.last_name = attrs.get('user.last_name', user.last_name)
    #
    #         user.save()
    #
    #     return profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

class PlaceSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'category', 'streetnum', 'street', 'city', 'country', 'image', 'owner', 'latitude', 'longitude','created_time')