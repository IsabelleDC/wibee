

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'about')
        # read_only_fields = ('date_joined',)
        # write_only_fields = ('password',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place