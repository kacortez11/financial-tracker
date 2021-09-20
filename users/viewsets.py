from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        print(request)
        queryset = User.objects.all()
        return queryset
