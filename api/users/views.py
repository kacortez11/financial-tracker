from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = User.objects.filter(id=user_id).first()
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.validated_data or serializer.errors)


@api_view(['POST'])
def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.validated_data or serializer.errors)


@api_view(['POST'])
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    return Response("success")
