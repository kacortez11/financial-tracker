from api.categories.models import Merchant
from rest_framework.viewsets import ModelViewSet

from api.categories.serializers.merchant_serializer import MerchantSerializer


class MerchantViewSet(ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        queryset = Merchant.objects.all()
        return queryset
