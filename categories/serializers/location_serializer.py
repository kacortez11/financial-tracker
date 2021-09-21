from rest_framework.serializers import ModelSerializer

from categories.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
