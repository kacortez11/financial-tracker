from django.db.models import (
    CharField,
    PROTECT,
    ForeignKey,
    BooleanField,
    DecimalField,
)

from api.core.models import BaseModel, BaseUserModel


class User(BaseModel):
    username = CharField(max_length=16, blank=False, null=False, unique=True)
    first_name = CharField(max_length=16, blank=False, null=False)
    last_name = CharField(max_length=16, blank=False, null=False)
    display_name = CharField(max_length=16, null=True)
    is_active = BooleanField(default=True)
    is_test = BooleanField(default=False)

    def __str__(self):
        return self.display_name or f"{self.first_name} {self.last_name}"


class Person(BaseUserModel):
    user = ForeignKey('users.User', PROTECT, null=False)
    first_name = CharField(max_length=32, blank=False, null=False)
    last_name = CharField(max_length=32, blank=False, null=False)
    display_name = CharField(max_length=64, null=True)

    def __str__(self):
        return self.display_name or f"{self.first_name} {self.last_name}"


class Subscription(BaseUserModel):
    DAILY = 1
    WEEKLY = 7
    FORTNIGHTLY = 14
    MONTHLY = 30
    QUARTERLY = 90
    ANNUALLY = 90
    FREQUENCY_OF_CHARGE_TYPES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (FORTNIGHTLY, 'Every two weeks'),
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (ANNUALLY, 'Annually')
    )

    category = ForeignKey(
        'categories.Category',
        PROTECT,
        related_name='subscription_category',
        null=False
    )
    amount_of_charge = DecimalField(
        decimal_places=2,
        max_digits=32,
        blank=False,
        null=False
    )
    frequency_of_charge = CharField(
        max_length=16,
        choices=FREQUENCY_OF_CHARGE_TYPES,
        default=MONTHLY,
        blank=False,
        null=False
    )
