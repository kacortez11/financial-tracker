from rest_framework.serializers import ModelSerializer

from api.transfers.models import Transfer


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
