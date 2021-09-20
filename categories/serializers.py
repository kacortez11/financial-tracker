from rest_framework.serializers import ModelSerializer

from categories.models import Category, Merchant, Location, Courier


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    #     extra_fields = ['subcategories']
    #
    # def get_field_names(self, declared_fields, info):
    #     expanded_fields = super(
    #         CategorySerializer,
    #         self
    #     ).get_field_names(declared_fields, info)
    #
    #     if getattr(self.Meta, 'extra_fields', None):
    #         return expanded_fields + self.Meta.extra_fields
    #     else:
    #         return expanded_fields
    #
    # def get_subcategories(self):
    #     return Category.objects.filter(parent=1)

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
