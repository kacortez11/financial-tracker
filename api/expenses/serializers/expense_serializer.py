from rest_framework.fields import JSONField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from api.categories.models import Category
from api.categories.serializers.category_serializer import CategorySerializer
from api.expenses.models import Expense, Share
from api.expenses.serializers.adulting_serializer import AdultingSerializer
from api.expenses.serializers.loan_credit_card_serializer import \
    LoanCreditCardSerializer
from api.expenses.serializers.meal_serializer import MealSerializer
from api.expenses.serializers.medical_serializer import MedicalSerializer
from api.expenses.serializers.online_shopping_serializer import \
    OnlineShoppingSerializer
from api.expenses.serializers.pet_serializer import PetSerializer
from api.expenses.serializers.share_serializer import ShareSerializer
from api.expenses.serializers.transportation_serializer import \
    TransportationSerializer
from api.modes_of_payment.models import ModeOfPayment
from api.modes_of_payment.serializer import ModeOfPaymentSerializer


class ExpenseSerializer(ModelSerializer):
    details = JSONField(binary=True, read_only=True)
    shared_with = ShareSerializer(many=True)
    adulting = AdultingSerializer(allow_null=True)
    loan = LoanCreditCardSerializer(allow_null=True)
    meal = MealSerializer(allow_null=True)
    medical = MedicalSerializer(allow_null=True)
    online_shopping = OnlineShoppingSerializer(allow_null=True)
    pet = PetSerializer(allow_null=True)
    transportation = TransportationSerializer(allow_null=True)
    # mode_of_payment = PrimaryKeyRelatedField(
    #     queryset=ModeOfPayment.objects.filter(user=1)
    # )
    # category = PrimaryKeyRelatedField(
    #     queryset=Category.objects.filter(
    #         user=1,
    #         transaction_type='expense',
    #         parent_id=1
    #     )
    # )
    # expense = PrimaryKeyRelatedField(
    #     queryset=Expense.objects.filter(is_reversal=False),
    #     validators=[UniqueValidator(queryset=Expense.objects.all())]
    # )

    class Meta:
        model = Expense
        fields = '__all__'

    def create(self, validated_data):
        shared_with = validated_data.pop('shared_with')
        details = validated_data.pop('details')
        instance = super().create(validated_data)
        instance.date_incurred = validated_data.get('date_incurred')
        instance.date_posted = validated_data.get(
            'date_posted',
            instance.date_incurred
        )

        instance.mode_of_payment = validated_data.get('mode_of_payment')
        instance.total_amount = validated_data.get('total_amount')
        instance.my_share = validated_data.get('my_share')
        instance.merchandise_total = validated_data.get('merchandise_total')
        instance.merchandise_discount = validated_data.get(
            'merchandise_discount'
        )
        instance.shipping_fee = validated_data.get('shipping_fee')
        instance.shipping_discount = validated_data.get('shipping_discount')
        instance.service_fee = validated_data.get('service_fee')
        instance.expected_cashback = validated_data.get('expected_cashback')
        instance.is_pending = validated_data.get('is_pending')
        instance.category = validated_data.get('category')
        instance.is_reversal = validated_data.get('is_reversal')
        instance.expense = validated_data.get('expense')
        instance.date_reversed = validated_data.get('date_reversed')

        instance.save()

        if shared_with is not None:
            for share in shared_with:
                Share.objects.create(
                    expense=instance.id,
                    shared_with=share.get('name'),
                    share=share.get('share'),
                    paid=share.get('paid')
                )

        if instance.category == 1: # Adulting
            pass
        elif instance.category == 2: #Meal
            pass
        elif instance.category == 3: #Transpo
            pass
        else:
            pass

        return instance

    def update(self, instance, validated_data):
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()

        return instance

    @staticmethod
    def _category_under_expense(_category):
        Category.objects.filter(type='expense', parent_id=1)
        return False
