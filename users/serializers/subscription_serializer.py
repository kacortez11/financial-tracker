from rest_framework.serializers import ModelSerializer

from users.models import Subscription


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
