from django.db.models import (
	ForeignKey, PROTECT, DecimalField,
	DateField, CheckConstraint, Q, F,
)

from api.core.models import BaseUserModel


class Transfer(BaseUserModel):
	date_incurred = DateField(blank=False, null=False)
	amount = DecimalField(
		decimal_places=2,
		max_digits=32,
		blank=False,
		null=False
	)
	transfer_fee = DecimalField(
		decimal_places=2,
		max_digits=32,
		default=0,
		blank=True,
		null=True
	)
	transfer_channel = ForeignKey(
		'categories.Category',
		PROTECT,
		related_name='transfer_channel_category',
		null=False
	)
	source = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		PROTECT,
		related_name='source',
		null=False
	)
	destination = ForeignKey(
		'modes_of_payment.ModeOfPayment',
		PROTECT,
		related_name='destination',
		null=False
	)

	class Meta:
		constraints = [
			CheckConstraint(
				name='source_different_from_destination',
				check=~Q(source=F('destination')),
			),
		]
