from rest_framework.serializers import ModelSerializer

from api.expenses.models import Medical


class MedicalSerializer(ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'
