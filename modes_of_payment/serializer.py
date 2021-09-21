from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import ModeOfPayment


class ModeOfPaymentSerializer(ModelSerializer):
    # subcategories = SerializerMethodField('get_subcategories')
    #
    # def get_subcategories(self, obj):
    #     test = ModeOfPayment.objects.filter(parent__id=getattr(obj, 'id'))
    #     return list(ModeOfPaymentSerializer(test, many=True).data)

    class Meta:
        model = ModeOfPayment
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.value = validated_data.get('value')

        if validated_data.get('label') == '':
            instance.label = validated_data.get('value').capitalize()
        else:
            instance.label = validated_data.get('label')

        if validated_data.get('debit'):
            instance.debit = True
            instance.interest_rate_per_annum = validated_data.get(
                'interest_rate_per_annum'
            )
            instance.interest_credited_at = validated_data.get(
                'interest_credited_at'
            )
            instance.frequency_of_interest_computation = validated_data.get(
                'frequency_of_interest_computation'
            )
            instance.frequency_of_interest_crediting = validated_data.get(
                'frequency_of_interest_crediting'
            )
            instance.days_in_a_year = validated_data.get('days_in_a_year')
            instance.minimum_maintaining_balance = validated_data.get(
                'minimum_maintaining_balance'
            )
        else:
            instance.cut_off = validated_data.get('cut_off')
            instance.limit = validated_data.get('limit')

        # if this is default, set all others to default false
        instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value')

        if validated_data.get('label') == '':
            instance.label = validated_data.get('value').capitalize()
        else:
            instance.label = validated_data.get('label')

        if validated_data.get('debit'):
            self.reset_credit(instance)
            instance.interest_rate_per_annum = validated_data.get(
                'interest_rate_per_annum',
                instance.interest_rate_per_annum
            )
            instance.interest_credited_at = validated_data.get(
                'interest_credited_at',
                instance.interest_credited_at
            )
            instance.frequency_of_interest_computation = validated_data.get(
                'frequency_of_interest_computation',
                instance.frequency_of_interest_computation
            )
            instance.frequency_of_interest_crediting = validated_data.get(
                'frequency_of_interest_crediting',
                instance.frequency_of_interest_crediting
            )
            instance.days_in_a_year = validated_data.get(
                'days_in_a_year',
                instance.days_in_a_year
            )
            instance.minimum_maintaining_balance = validated_data.get(
                'minimum_maintaining_balance',
                instance.minimum_maintaining_balance
            )
        else:
            self.reset_debit(instance)
            instance.cut_off = validated_data.get('cut_off', instance.cut_off)
            instance.limit = validated_data.get('limit', instance.limit)

        # if this is default, set all others to default false
        instance.save()

        return instance

    @staticmethod
    def reset_credit(instance):
        instance.debit = True
        instance.cut_off = None
        instance.limit = None

    @staticmethod
    def reset_debit(instance):
        instance.debit = False
        instance.interest_rate_per_annum = None
        instance.interest_credited_at = None
        instance.frequency_of_interest_computation = None
        instance.frequency_of_interest_crediting = None
        instance.days_in_a_year = None
        instance.minimum_maintaining_balance = None
