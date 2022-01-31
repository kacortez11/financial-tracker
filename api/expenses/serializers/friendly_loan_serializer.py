from rest_framework.serializers import ModelSerializer

from api.expenses.models import FriendlyLoan


class FriendlyLoanSerializer(ModelSerializer):
    class Meta:
        model = FriendlyLoan
        fields = '__all__'
