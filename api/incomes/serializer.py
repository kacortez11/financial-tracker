from rest_framework.serializers import ModelSerializer

from api.incomes.models import Income
from api.invoices.models import Invoice


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.date_incurred = validated_data.get('date_incurred')
        instance.source = validated_data.get('source')
        instance.amount = validated_data.get('amount')
        instance.details = validated_data.get('details')
        instance.mode_of_payment = validated_data.get('mode_of_payment')
        instance.payment_invoice = validated_data.get('invoice')

        instance.save()

        self.update_invoice(validated_data)

        return instance

    def update(self, instance, validated_data):
        instance.date_incurred = validated_data.get(
            'date_incurred',
            instance.date_incurred
        )
        instance.source = validated_data.get('source', instance.source)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.details = validated_data.get('details', instance.details)
        instance.mode_of_payment = validated_data.get(
            'mode_of_payment',
            instance.mode_of_payment
        )
        instance.payment_invoice = validated_data.get(
            'invoice',
            instance.payment_invoice
        )

        instance.save()

        self.update_invoice(validated_data)

        return instance

    @staticmethod
    def update_invoice(validated_data):
        if validated_data.get('invoice'):
            invoice_obj = validated_data.get('invoice')
            invoice = Invoice.objects.filter(id=invoice_obj.id).first()
            if invoice.total_amount == validated_data.get('amount'):
                invoice.paid = True
                invoice.save()
