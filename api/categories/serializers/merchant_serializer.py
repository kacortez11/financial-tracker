from rest_framework.serializers import ModelSerializer

from api.categories.models import Merchant


class MerchantSerializer(ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
