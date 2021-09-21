from rest_framework.viewsets import ModelViewSet

from users.models import Subscription
from users.serializers.subscription_serializer import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        queryset = Subscription.objects.all()
        return queryset
