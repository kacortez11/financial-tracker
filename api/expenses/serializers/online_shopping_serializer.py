from rest_framework.serializers import ModelSerializer

from api.expenses.models import OnlineShopping


class OnlineShoppingSerializer(ModelSerializer):
    class Meta:
        model = OnlineShopping
        fields = '__all__'
