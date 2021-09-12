from django.db.models import CharField, ForeignKey, PROTECT, DecimalField, DateField

from core.models import BaseModel, BaseUserModel


class Invoice(BaseUserModel):
	date_incurred = DateField(blank=False)
	bill_to = CharField(max_length=64, null=False)
	description = CharField(max_length=32, null=False)
	subtotal = DecimalField(decimal_places=2, max_digits=32, blank=False)
	total_amount = DecimalField(decimal_places=2, max_digits=32, blank=False)
