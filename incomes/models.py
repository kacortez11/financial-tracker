from django.db.models import ForeignKey, PROTECT, DecimalField, TextField, DateField

from core.models import BaseModel, BaseUserModel


class Income(BaseUserModel):
	date_incurred = DateField(blank=False)
	source = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='source_of_income'
	)
	amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
	details = TextField(null=True)
	mode_of_payment = ForeignKey(
		'mode_of_payments.ModeOfPayment',
		PROTECT,
		related_name='income_mode_of_payment'
	)
