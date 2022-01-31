from rest_framework.fields import JSONField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from api.categories.models import Category
from api.categories.serializers.category_serializer import CategorySerializer
from api.expenses.models import Expense, Share
from api.expenses.serializers.adulting_serializer import AdultingSerializer
from api.expenses.serializers.friendly_loan_serializer import \
    FriendlyLoanSerializer
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
    shared_with = ShareSerializer(many=True, required=False, allow_null=True)
    adulting = AdultingSerializer(allow_null=True, required=False)
    loan = LoanCreditCardSerializer(allow_null=True, required=False)
    friendly_loan = FriendlyLoanSerializer(allow_null=True, required=False)
    meal = MealSerializer(allow_null=True, required=False)
    medical = MedicalSerializer(allow_null=True, required=False)
    online_shopping = OnlineShoppingSerializer(allow_null=True, required=False)
    pet = PetSerializer(allow_null=True, required=False)
    transportation = TransportationSerializer(allow_null=True, required=False)
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
        shared_with = validated_data.pop('shared_with', None)
        details = validated_data.pop('details', None)
        adulting = validated_data.pop('adulting', None)
        loan = validated_data.pop('loan', None)
        friendly_loan = validated_data.pop('loan', None)
        meal = validated_data.pop('meal', None)
        medical = validated_data.pop('medical', None)
        online_shopping = validated_data.pop('online_shopping', None)
        pet = validated_data.pop('pet', None)
        transportation = validated_data.pop('transportation', None)

        if validated_data.get('total_amount') != (
                validated_data.get('merchandise_total') -
                validated_data.get('merchandise_discount') +
                validated_data.get('shipping_fee') -
                validated_data.get('shipping_discount') +
                validated_data.get('service_fee')
        ):
            return False

        instance = super().create(validated_data)
        instance.date_posted = validated_data.get(
            'date_posted',
            instance.date_incurred
        )
        if shared_with is not None and validated_data.get('my_share') is None:
            return False # return error if shared but my_share is empty
        # instance.save()

        if shared_with is not None:
            for share in shared_with:
                share['expense'] = instance
                Share.objects.create(share)

        expense_categories = self._category_under_expense(1).values_list('id', flat=True)
        if instance.category_id in expense_categories:
            if instance.category_id == Expense.MEAL:
                meal['expense'] = instance
                MealSerializer().create(meal)

            elif instance.category_id == Expense.PET:
                pet['expense'] = instance
                MealSerializer().create(pet)

            elif instance.category_id == Expense.TRANSPORTATION:
                transportation['expense'] = instance
                MealSerializer().create(transportation)

            elif instance.category_id == Expense.ADULTING:
                adulting['expense'] = instance
                AdultingSerializer().create(adulting)

            elif instance.category_id == Expense.LOAN:
                loan['expense'] = instance
                LoanCreditCardSerializer().create(loan)

            elif instance.category_id == Expense.FRIENDLY_LOAN:
                loan['expense'] = instance
                FriendlyLoanSerializer().create(loan)

            elif instance.category_id == Expense.MEDICAL:
                medical['expense'] = instance
                MedicalSerializer().create(medical)

            elif instance.category_id == Expense.HOBBIES:
                adulting['expense'] = instance
                AdultingSerializer().create(adulting)

            elif instance.category_id == Expense.HOBBIES:
                adulting['expense'] = instance
                AdultingSerializer().create(adulting)
        else:
            return False

        return instance

    def update(self, instance, validated_data):
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()

        return instance

    @staticmethod
    def _category_under_expense(_category):
        return Category.objects.filter(parent_id=_category)

    @staticmethod
    def computation_valid(data):
        return data.get('total_amount') != (
                data.get('merchandise_total') -
                data.get('merchandise_discount') +
                data.get('shipping_fee') -
                data.get('shipping_discount') +
                data.get('service_fee')
        )
