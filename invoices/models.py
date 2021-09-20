from django.db.models import CharField, ForeignKey, PROTECT, DecimalField, DateField

from core.models import BaseModel, BaseUserModel


class Invoice(BaseUserModel):
	bill_to = ForeignKey(
		'persons.Person',
		PROTECT,
		related_name='person_to_invoice',
		null=False
	)
	description = CharField(max_length=32, null=False)
	subtotal = DecimalField(decimal_places=2, max_digits=32, blank=False)
	total_amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
