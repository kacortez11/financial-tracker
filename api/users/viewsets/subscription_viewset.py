from rest_framework.viewsets import ModelViewSet

from api.users.models import Subscription
from api.users.serializers.subscription_serializer import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        queryset = Subscription.objects.all()
        return queryset
