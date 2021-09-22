from django.db.models import (
	ForeignKey, PROTECT, DecimalField, TextField,
	DateField,
)

from api.core.models import BaseUserModel


class Income(BaseUserModel):
    date_incurred = DateField(blank=False, null=False)
    source = ForeignKey(
        'categories.Category',
        PROTECT,
        related_name='source_of_income'
    )
    amount = DecimalField(
        decimal_places=2,
        max_digits=32,
        blank=False,
        null=False
    )
    details = TextField(null=True)
    mode_of_payment = ForeignKey(
        'modes_of_payment.ModeOfPayment',
        PROTECT,
        related_name='income_mode_of_payment',
        null=False
    )
    invoice = ForeignKey(
        'invoices.Invoice',
        PROTECT,
        related_name='payment_invoice',
        null=True
    )
