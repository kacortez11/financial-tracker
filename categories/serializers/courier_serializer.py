from rest_framework.serializers import ModelSerializer

from categories.models import Courier


class CourierSerializer(ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
