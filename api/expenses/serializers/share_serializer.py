from rest_framework.serializers import ModelSerializer

from api.expenses.models import Share


class ShareSerializer(ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'
