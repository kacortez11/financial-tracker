from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    PositiveIntegerField,
    URLField,
    PositiveSmallIntegerField,
    OneToOneField, PROTECT,
)


from core.models import BaseModel, BaseUserModel


class ModeOfPayment(BaseUserModel):
    CASH = 'cash'
    TRADITIONAL_BANK = 'traditional_bank'
    DIGITAL = 'digital_bank'
    EWALLET = 'e_wallet'
    INAPP_WALLET = 'in_app_wallet'

    TYPES = (
        (CASH, 'Cash'),
        (TRADITIONAL_BANK, 'Bank'),
        (DIGITAL, 'Digital'),
        (EWALLET, 'E-wallet'),
        (INAPP_WALLET, 'App Integrated Wallet'),
    )

    THREE_SIX_FIVE = 365
    THREE_SIXTY = 365
    DAYS_IN_A_YEAR = (
        (THREE_SIX_FIVE, '365'),
        (THREE_SIXTY, '360')
    )
    DAILY = 1
    WEEKLY = 7
    FORTNIGHTLY = 14
    MONTHLY = 30
    QUARTERLY = 90
    FREQUENCY_OF_INTEREST_TYPES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (FORTNIGHTLY, 'Every two weeks'),
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly')
    )

    SOM = 1
    EOM = 30

    value = CharField(max_length=32, null=False)
    label = CharField(max_length=32, null=False)
    type = CharField(max_length=32, choices=TYPES, null=False)
    debit = BooleanField(default=True)  # False means credit
    is_active = BooleanField(default=True)
    date_deactivated = DateField(null=True)
    priority = PositiveIntegerField(default=99)
    default = BooleanField(default=False)

    currency = CharField(max_length=4, default='PHP', null=False)
    starting_balance = DecimalField(decimal_places=2, max_digits=32, default=0)

    # Savings related
    interest_rate_per_annum = DecimalField(
        decimal_places=2,
        max_digits=5,
        default=0,
        blank=True,
        null=True
    )
    interest_credited_at = PositiveSmallIntegerField(
        default=SOM,
        blank=True,
        null=True
    )
    frequency_of_interest_computation = PositiveSmallIntegerField(
        choices=FREQUENCY_OF_INTEREST_TYPES,
        blank=True,
        null=True
    )
    frequency_of_interest_crediting = PositiveSmallIntegerField(
        choices=FREQUENCY_OF_INTEREST_TYPES,
        blank=True,
        null=True
    )
    days_in_a_year = PositiveSmallIntegerField(
        choices=DAYS_IN_A_YEAR,
        blank=True,
        null=True
    )
    minimum_maintaining_balance = DecimalField(
        decimal_places=2,
        max_digits=32,
        default=0
    )

    # Credit related
    cut_off = PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    limit = DecimalField(
        decimal_places=2,
        max_digits=32,
        blank=True,
        null=True
    )


class Accounts(BaseUserModel):
    mop = OneToOneField(
        'ModeOfPayment',
        PROTECT,
        to_field='id'
    )
    branch = CharField(max_length=64, null=True)
    account_number = CharField(max_length=32, null=True)
    website = URLField(max_length=256, null=True)
    login_url = CharField(max_length=32, null=True)
