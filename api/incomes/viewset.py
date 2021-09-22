from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.incomes.models import Income
from api.incomes.serializer import IncomeSerializer


class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return Income.objects.all()

    @action(detail=False)
    def report(self, request, **kwargs):
        queryset = Income.objects.filter(user_id=1).aggregate(Sum(
            'amount'))
        return Response(queryset['amount__sum'])
