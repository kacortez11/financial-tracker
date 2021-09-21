
from rest_framework.viewsets import ModelViewSet

from invoices.models import Invoice
from invoices.serializer import InvoiceSerializer


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()
