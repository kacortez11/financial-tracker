from rest_framework.serializers import ModelSerializer

from .models import BaseUserModel


class BaseUserModelSerializer(ModelSerializer):
    class Meta:
        model = BaseUserModel
        fields = ['user_id']
