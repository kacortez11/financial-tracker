from api.expenses.models import Meal
from rest_framework.viewsets import ModelViewSet

from api.expenses.serializers.meal_serializer import MealSerializer


class MealViewSet(ModelViewSet):
    serializer_class = MealSerializer

    def get_queryset(self):
        queryset = Meal.objects.all()
        return queryset
