from rest_framework.serializers import ModelSerializer

from api.expenses.models import Adulting


class AdultingSerializer(ModelSerializer):
    class Meta:
        model = Adulting
        fields = '__all__'
