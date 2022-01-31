from enum import Enum

from django.db.models import (
	BooleanField, ForeignKey, PROTECT, DateField, DecimalField,
	UniqueConstraint, CharField, OneToOneField, TextField, CheckConstraint, Q,
	F,
)

from api.core.models import BaseModel, BaseUserModel


class Expense(BaseUserModel):
	MEAL = 4
	PET = 5
	TRANSPORTATION = 6
	ADULTING = 7
	LOAN = 8
	FRIENDLY_LOAN = 9
	MEDICAL = 10
	HOBBIES = 11
	ALIGNMENT = 12

	ExpenseCategories = (
		(MEAL, 'Meal'),
		(PET, 'Pet'),
		(TRANSPORTATION, 'Transportation'),
		(ADULTING, 'Adulting'),
		(LOAN, 'Loan'),
		(MEDICAL, 'Medical'),
		(HOBBIES, 'Hobbies'),
		(ALIGNMENT, 'Alignment')
	)

	date_incurred = DateField(blank=False, null=False)
	date_posted = DateField(blank=True, null=True)
	mode_of_payment = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		on_delete=PROTECT,
		related_name='expense_mode_of_payment',
		null=False
	)
	total_amount = DecimalField(
		decimal_places=2,
		max_digits=32,
		blank=False,
		null=True
	)
	my_share = DecimalField(decimal_places=2, max_digits=32, null=True)
	merchandise_total = DecimalField(decimal_places=2, max_digits=32, null=True)
	merchandise_discount = DecimalField(
		decimal_places=2,
		max_digits=32,
		default=0
	)
	shipping_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	shipping_discount = DecimalField(decimal_places=2, max_digits=32, default=0)
	service_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	expected_cashback = DecimalField(decimal_places=2, max_digits=32, default=0)
	is_pending = BooleanField(default=False, null=False)
	category = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='expense_category',
		choices=ExpenseCategories,
		null=False
	)
	is_reversal = BooleanField(default=False)
	expense = OneToOneField(
		'Expense',
		on_delete=PROTECT,
		related_name='reversed_expense',
		null=True
	)
	date_reversed = DateField(default=None, null=True)

	class Meta:
		constraints = [
			CheckConstraint(
				name='incurred_before_posted',
				check=Q(date_posted__gte=F('date_incurred')),
			),
			CheckConstraint(
				name='incurred_before_reversed',
				check=Q(date_reversed__gte=F('date_incurred')),
			),
			CheckConstraint(
				name='posted_before_reversed',
				check=Q(date_reversed__gte=F('date_posted')),
			),
			CheckConstraint(
				name='my_share_lte_to_total_amount',
				check=Q(my_share__lte=F('total_amount')),
			),
			CheckConstraint(
				name='total_amount_computation_valid',
				check=Q(total_amount__lte=F('total_amount')),
			),
		]


class Share(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		on_delete=PROTECT,
		related_name='shared_expense',
		null=False
	)
	shared_with = ForeignKey(
		'users.Person',
		on_delete=PROTECT,
		related_name='shared_expense_person',
		null=False
	)
	share = DecimalField(
		decimal_places=2,
		max_digits=32,
		blank=True,
		null=True
	)
	paid = BooleanField(default=False)
	invoice = OneToOneField(
		'invoices.Invoice',
		on_delete=PROTECT,
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
		on_delete=PROTECT,
		related_name='meal_expense',
		null=True
	)
	type = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='meal_type_category',
		null=False
	)
	restaurant = ForeignKey(
		'categories.Merchant',
		on_delete=PROTECT,
		related_name='meal_merchant',
		null=False
	)
	particulars = TextField(null=False)
	order_mode = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='meal_order_mode_category',
		null=False
	)


class Transportation(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		on_delete=PROTECT,
		related_name='transportation_expense',
		null=False
	)
	type = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='transportation_mode_category',
		null=False
	)
	origin = ForeignKey(
		'categories.Location',
		on_delete=PROTECT,
		related_name='transportation_origin',
		null=False
	)
	destination = ForeignKey(
		'categories.Location',
		on_delete=PROTECT,
		related_name='transportation_destination',
		null=False
	)


class Medical(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		on_delete=PROTECT,
		related_name='medical_expense',
		null=False
	)
	transaction = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='medical_transaction_category',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		on_delete=PROTECT,
		related_name='medical_merchant',
		null=False
	)


class Adulting(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		on_delete=PROTECT,
		related_name='adulting_expense',
		null=False
	)
	type = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='adulting_category',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		on_delete=PROTECT,
		related_name='adulting_merchant',
		null=True
	)


class LoanCreditCard(BaseUserModel):
	expense = OneToOneField(
		'expenses.Expense',
		on_delete=PROTECT,
		related_name='loan_expense',
		null=False
	)
	charge_type = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='credit_charge_type',
		null=False
	)
	credit_account = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		on_delete=PROTECT,
		related_name='credit_account',
		null=False
	)


class FriendlyLoan(BaseUserModel):
	expense = OneToOneField(
		'Expense',
		on_delete=PROTECT,
		related_name='friendly_loan_expense',
		null=False
	)
	friend = ForeignKey(
		'users.Person',
		on_delete=PROTECT,
		related_name='friend',
		null=False
	)
	date_to_pay = DateField(null=False)
	details = TextField(null=True)


class OnlineShopping(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		on_delete=PROTECT,
		related_name='online_shopping_expense',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		on_delete=PROTECT,
		related_name='online_shopping_platform',
		null=False
	)
	purchase_category = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='purchase_category',
		null=False
	)
	particulars = TextField(null=False)
	courier = ForeignKey(
		'categories.Courier',
		on_delete=PROTECT,
		related_name='courier',
		null=True
	)


class Pet(BaseUserModel):
	expense = ForeignKey(
		'Expense',
		on_delete=PROTECT,
		related_name='pet_expense',
		null=False
	)
	merchant = ForeignKey(
		'categories.Merchant',
		on_delete=PROTECT,
		related_name='pet_merchant',
		null=False
	)
	purchase_category = ForeignKey(
		'categories.Category',
		on_delete=PROTECT,
		related_name='pet_purchase_category',
		null=False
	)
	particulars = TextField(null=False)
	online_transaction = BooleanField(default=True)
	courier = ForeignKey(
		'categories.Courier',
		on_delete=PROTECT,
		related_name='pet_purchase_courier',
		null=True
	)
