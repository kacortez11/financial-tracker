from django.db.models import (
	CharField,
	ForeignKey,
	PROTECT,
	DecimalField,
	DateField, BooleanField,
)
from django.utils import timezone

from core.models import BaseModel, BaseUserModel


class Invoice(BaseUserModel):
	due_date = DateField(default=timezone.now, blank=False, null=False)
	bill_to = ForeignKey(
		'users.Person',
		PROTECT,
		related_name='person_to_invoice',
		null=False
	)
	description = CharField(max_length=128, null=True)
	subtotal = DecimalField(
		decimal_places=2,
		max_digits=32,
		blank=False,
		null=False
	)
	less_amount = DecimalField(
		decimal_places=2,
		max_digits=32,
		default=0,
		blank=True,
		null=False
	)
	total_amount = DecimalField(
		decimal_places=2,
		max_digits=32,
		blank=False,
		null=False
	)
	paid = BooleanField(default=False, null=False)

	def __str__(self):
		return f"Invoice for {self.bill_to.__str__()} due on {self.due_date}"
