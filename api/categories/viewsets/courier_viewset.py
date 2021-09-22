from api.categories.models import Courier
from rest_framework.viewsets import ModelViewSet

from api.categories.serializers.courier_serializer import CourierSerializer


class CourierViewSet(ModelViewSet):
    serializer_class = CourierSerializer

    def get_queryset(self):
        queryset = Courier.objects.all()
        return queryset
