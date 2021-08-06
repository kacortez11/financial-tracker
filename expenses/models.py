from django.db.models import (
	BooleanField, ForeignKey, PROTECT, DateField, DecimalField
)

from core.models import BaseModel, BaseUserModel


class Expense(BaseUserModel):
	date_incurred = DateField(blank=False)
	date_posted = DateField(blank=False)
	mode_of_payment = ForeignKey(
		'mode_of_payments.ModeOfPayment',
		PROTECT,
		related_name='expense_mode_of_payment_id', null=True
	)
	total_amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
	my_share = DecimalField(decimal_places=2, max_digits=32)
	merchandise_total = DecimalField(decimal_places=2, max_digits=32)
	merchandise_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	shipping_fee = DecimalField(decimal_places=2, max_digits=32)
	shipping_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	service_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	expected_cashback = DecimalField(decimal_places=2, max_digits=32, default=0)
	pending = BooleanField(default=False)
	reversal = BooleanField(default=False)
	reversal_id = ForeignKey(
		'Expense',
		PROTECT,
		related_name='expense_id', null=True
	)
	category_id = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='expense_id', null=True
	)


