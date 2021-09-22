from rest_framework.serializers import ModelSerializer

from api.expenses.models import Pet


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
