from rest_framework.serializers import ModelSerializer

from transfers.models import Transfer


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def create(self, validated_data):
        if not self.source_different_from_destination(validated_data):
            raise Exception

        instance = super().create(validated_data)

        instance.save()

        return instance

    def update(self, instance, validated_data):
        if not self.source_different_from_destination(validated_data):
            raise Exception

        instance.source = validated_data.get('source')
        instance.destination = validated_data.get('destination')

        instance.save()

        return instance

    @staticmethod
    def source_different_from_destination(data):
        # data.get('source') != data.get('destination') or
        # (instance is not None and # update
        # (instance.source != data.get('destination') or
        # instance.destination != data.get('source'))
        # )
        return data.get('source') != data.get('destination')
