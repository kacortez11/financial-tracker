from rest_framework.viewsets import ModelViewSet

from api.invoices.models import Invoice
from api.invoices.serializer import InvoiceSerializer


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()
