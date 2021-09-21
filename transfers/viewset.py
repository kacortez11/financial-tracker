from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        if request.data.get('destination') == request.data.get('source'):
            return Response(
                data="Destination cannot be the same as source.",
                status=HTTPStatus.CONFLICT
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=HTTPStatus.CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        if request.data.get('destination') == request.data.get('source'):
            return Response(
                data="Destination cannot be the same as source.",
                status=HTTPStatus.CONFLICT
            )
