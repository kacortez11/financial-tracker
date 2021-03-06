from rest_framework.viewsets import ModelViewSet

from api.transfers.models import Transfer
from api.transfers.serializer import TransferSerializer


class TransferViewSet(ModelViewSet):
    serializer_class = TransferSerializer

    def get_queryset(self):
        return Transfer.objects.all()
