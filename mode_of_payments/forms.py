from django.forms import ModelForm

from .models import ModeOfPayment


class ModeofPaymentForm(ModelForm):
	class Meta:
		model = ModeOfPayment
		fields = [
			'value',
			'label',
			'type',
			'debit',
			'is_active',
			'priority',
			'default',
			'currency',
			'starting_balance',
			'type'
		]