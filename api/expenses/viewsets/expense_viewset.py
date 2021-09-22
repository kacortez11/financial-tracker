from api.expenses.models import Expense
from rest_framework.viewsets import ModelViewSet

from api.expenses.serializers.expense_serializer import ExpenseSerializer


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.all()
        return queryset
