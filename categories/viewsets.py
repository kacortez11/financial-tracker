from rest_framework import status
from rest_framework.response import Response

from categories.models import Category
from .serializers import CategorySerializer
from rest_framework.viewsets import ViewSet, ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data or serializer.errors)

    def retrieve(self, request, *args, **kwargs):
        subcategories = []
        if request.query_params.get('show_subcategories'):
            subcategories = Category.objects.filter(
                parent_id=self.kwargs.get('pk')
            )
            subcategories_serializer = self.get_serializer(
                subcategories,
                many=True
            )
            subcategories = list(subcategories_serializer.data)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer.data['children'] = subcategories
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
