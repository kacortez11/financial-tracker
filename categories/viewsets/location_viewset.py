from categories.models import Location
from rest_framework.viewsets import ModelViewSet

from categories.serializers.location_serializer import LocationSerializer


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset
