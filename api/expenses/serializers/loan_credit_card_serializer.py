from rest_framework.serializers import ModelSerializer

from api.expenses.models import LoanCreditCard


class LoanCreditCardSerializer(ModelSerializer):
    class Meta:
        model = LoanCreditCard
        fields = '__all__'
