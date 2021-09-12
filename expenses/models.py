from django.db.models import (
	BooleanField, ForeignKey, PROTECT, DateField, DecimalField, UniqueConstraint, CharField, OneToOneField
)

from core.models import BaseModel, BaseUserModel
from invoices.models import Invoice


class Expense(BaseUserModel):
	date_incurred = DateField(blank=False)
	date_posted = DateField(blank=False)
	mode_of_payment = ForeignKey(
		'mode_of_payments.ModeOfPayment',
		PROTECT,
		related_name='expense_mode_of_payment', null=True
	)
	total_amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
	my_share = DecimalField(decimal_places=2, max_digits=32)
	merchandise_total = DecimalField(decimal_places=2, max_digits=32)
	merchandise_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	shipping_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	shipping_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	service_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	expected_cashback = DecimalField(decimal_places=2, max_digits=32, default=0)
	is_pending = BooleanField(default=False)
	is_reversal = BooleanField(default=False)
	category = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='expense_category',
		null=True
	)


class Reversal(Expense):
	expense = ForeignKey(
		'Expense',
		PROTECT,
		related_name='expense_for_reversal',
		null=True
	)
	date_reversed = DateField(null=True)

	class Meta:
		constraints = [
			UniqueConstraint(
				fields=['expense'],
				name='unique_expense_for_reversal'
			),
		]


class Share(BaseModel):
	expense = ForeignKey(
		'Expense',
		PROTECT,
		related_name='shared_expense',
		null=False
	)
	shared_with = CharField(max_length=32, null=False)
	share = DecimalField(decimal_places=2, max_digits=32, null=False)
	paid = BooleanField(default=False)
	invoice = ForeignKey(
		'invoices.Invoice',
		PROTECT,
		related_name='share_invoice',
		null=True
	)
