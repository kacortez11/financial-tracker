from rest_framework.viewsets import ModelViewSet

from .models import ModeOfPayment
from .serializer import ModeOfPaymentSerializer


class ModeOfPaymentViewSet(ModelViewSet):
    serializer_class = ModeOfPaymentSerializer

    def get_queryset(self):
        return ModeOfPayment.objects.filter(user_id=1)
