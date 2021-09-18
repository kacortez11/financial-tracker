from django.db.models import CharField, PROTECT, ForeignKey

from core.models import BaseModel, BaseUserModel


class User(BaseModel):
    username = CharField(max_length=16, blank=False, null=False)
    first_name = CharField(max_length=16, blank=False, null=False)
    last_name = CharField(max_length=16, blank=False, null=False)
    display_name = CharField(max_length=16, null=True)


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
    frequency_of_charge = CharField(
        max_length=16,
        choices=FREQUENCY_OF_CHARGE_TYPES,
        default=MONTHLY,
        blank=False,
        null=False
    )
