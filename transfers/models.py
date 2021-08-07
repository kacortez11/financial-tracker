from django.db.models import CharField, ForeignKey, PROTECT, DecimalField, DateField

from core.models import BaseModel, BaseUserModel


class Transfer(BaseUserModel):
	date_incurred = DateField(blank=False)
	amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
	transfer_fee = DecimalField(decimal_places=2, max_digits=32, default=0)
	transfer_channel = CharField(max_length=32, null=False)
	source = ForeignKey('mode_of_payments.ModeOfPayment', PROTECT, related_name='source')
	destination = ForeignKey('mode_of_payments.ModeOfPayment', PROTECT, related_name='destination')
