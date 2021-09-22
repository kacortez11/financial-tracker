from api.categories.models import Category
from rest_framework.viewsets import ModelViewSet

from api.categories.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
