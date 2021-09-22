from rest_framework.viewsets import ModelViewSet

from api.users.models import User
from api.users.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
