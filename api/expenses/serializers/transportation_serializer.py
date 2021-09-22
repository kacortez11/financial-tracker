from rest_framework.serializers import ModelSerializer

from api.expenses.models import Transportation


class TransportationSerializer(ModelSerializer):
    class Meta:
        model = Transportation
        fields = '__all__'
