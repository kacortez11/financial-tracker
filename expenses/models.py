from django.db.models import (
	BooleanField, ForeignKey, PROTECT, DateField, DecimalField, UniqueConstraint, CharField, OneToOneField, TextField
)

from core.models import BaseModel, BaseUserModel
from invoices.models import Invoice


class Expense(BaseUserModel):
	date_incurred = DateField(blank=False)
	date_posted = DateField(blank=False)
	mode_of_payment = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		PROTECT,
		related_name='expense_mode_of_payment',
		null=False
	)
	total_amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
	my_share = DecimalField(decimal_places=2, max_digits=32)
	merchandise_total = DecimalField(decimal_places=2, max_digits=32)
	merchandise_discount = DecimalField(
		decimal_places=2,
		max_digits=32,
		default=0
	)
	shipping_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	shipping_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	service_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	expected_cashback = DecimalField(decimal_places=2, max_digits=32, default=0)
	is_pending = BooleanField(default=False)
	category = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='expense_category',
		null=False
	)
	is_reversal = BooleanField(default=False)
	expense = OneToOneField(
		'Expense',
		PROTECT,
		related_name='revered_expense',
		null=True
	)
	date_reversed = DateField(null=True)


class Share(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		PROTECT,
		related_name='shared_expense',
		null=False
	)
	shared_with = ForeignKey(
		'persons.Person',
		PROTECT,
		related_name='shared_expense_person',
		null=False
	)
	share = DecimalField(decimal_places=2, max_digits=32, null=False)
	paid = BooleanField(default=False)
	invoice = OneToOneField(
		'invoices.Invoice',
		PROTECT,
		related_name='share_invoice',
		null=True
	)

	class Meta:
		constraints = [
			UniqueConstraint(
				fields=['expense', 'shared_with'],
				name='unique_shared_expense_person'
			),
		]


class Meal(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		PROTECT,
		related_name='meal_expense',
		null=False
	)
	type = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='meal_type_category',
		null=False
	)
	restaurant = ForeignKey(
		'categories.Merchant',
		PROTECT,
		related_name='meal_merchant',
		null=False
	)
	particulars = TextField(null=False)
	order_mode = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='meal_order_mode_category',
		null=False
	)


class Transportation(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		PROTECT,
		related_name='transportation_expense',
		null=False
	)
	type = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='transportation_mode_category',
		null=False
	)
	origin = ForeignKey(
		'categories.Destination',
		PROTECT,
		related_name='transportation_origin',
		null=False
	)
	destination = ForeignKey(
		'categories.Destination',
		PROTECT,
		related_name='transportation_destination',
		null=False
	)


class Medical(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		PROTECT,
		related_name='medical_expense',
		null=False
	)
	transaction = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='medical_transaction_category',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		PROTECT,
		related_name='medical_merchant',
		null=False
	)


class Adulting(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		PROTECT,
		related_name='adulting_expense',
		null=False
	)
	type = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='adulting_category',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		PROTECT,
		related_name='adulting_merchant',
		null=True
	)


class LoanCreditCard(BaseUserModel):
	adulting = ForeignKey(
		'Adulting',
		PROTECT,
		related_name='adulting',
		null=False
	)
	charge_type = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='credit_charge_type',
		null=False
	)
	credit_account = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		PROTECT,
		related_name='credit_account',
		null=False
	)


class OnlineShopping(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		PROTECT,
		related_name='online_shopping_expense',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		PROTECT,
		related_name='online_shopping_platform',
		null=False
	)
	purchase_category = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='purchase_category',
		null=False
	)
	particulars = TextField(null=False)
	courier = ForeignKey(
		'categories.Courier',
		PROTECT,
		related_name='courier',
		null=True
	)


class Cat(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		PROTECT,
		related_name='cat_expense',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		PROTECT,
		related_name='cat_merchant',
		null=False
	)
	purchase_category = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='cat_purchase_category',
		null=False
	)
	particulars = TextField(null=False)
	online_transaction = BooleanField(default=True)
	courier = ForeignKey(
		'categories.Courier',
		PROTECT,
		related_name='cat_purchase_courier',
		null=True
	)
