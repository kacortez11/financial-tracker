from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from categories.models import Category, Merchant, Location, Courier


class CategorySerializer(ModelSerializer):
    subcategories = SerializerMethodField('get_subcategories')

    def get_subcategories(self, obj):
        test = Category.objects.filter(parent__id=getattr(obj, 'id'))
        return list(CategorySerializer(test, many=True).data)

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.transaction_type = validated_data.get('transaction_type')
        instance.category = validated_data.get('category')
        if validated_data.get('description') == '':
            instance.description = self._build_description(
                instance.transaction_type,
                instance.category
            )
        else:
            instance.description = validated_data.get('description')

        instance.has_subcategory = validated_data.get('has_subcategory')
        instance.parent = validated_data.get('parent')
        instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.transaction_type = validated_data.get(
            'transaction_type',
            instance.transaction_type
        )
        instance.category = validated_data.get('category', instance.category)

        if validated_data.get('description') == '':
            instance.description = self._build_description(
                instance.transaction_type,
                instance.category
            )
        else:
            instance.description = validated_data.get('description')

        instance.has_subcategory = validated_data.get(
            'has_subcategory',
            instance.has_subcategory
        )
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()

        return instance

    @staticmethod
    def _build_description(_type, _category):
        if _type.lower() == _category.lower():
            return None

        return f"{_type.capitalize()}s related to {_category.capitalize()}"


class MerchantSerializer(ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CourierSerializer(ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
