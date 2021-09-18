from django.forms import ModelForm, RadioSelect, Textarea, TextInput

from core.forms import *
from .models import ModeOfPayment


class ModeofPaymentForm(ModelForm):
    class Meta:
        model = ModeOfPayment
        fields = [
            'value',
            'label',
            'type',
            'debit',
            'is_active',
            'priority',
            'default',
            'currency',
            'starting_balance',
            'interest_rate_per_annum',
            'interest_credited_at',
            # 'frequency_of_interest_computation',
            # 'frequency_of_interest_crediting',
            'days_in_a_year',
            'minimum_maintaining_balance'
        ]


class RawModeOfPayment(Form):
    value = CharField(
        required=False,
        label='',
        widget=TextInput(attrs={
            'placeholder': 'Value'
        })
    )
    label = CharField()
    type = CharField()
    debit = BooleanField(initial=True, widget=RadioSelect)
    is_active = BooleanField(initial=True)
    date_deactivated = DateField(required=False)
    priority = IntegerField(initial=99)
    default = BooleanField(initial=False)

    currency = CharField(initial='PHP')
    starting_balance = DecimalField(initial=0)
    # Savings related
    interest_rate_per_annum = DecimalField(required=False)
    interest_credited_at = IntegerField(required=False, label='Day of the month interest is credited at')
    frequency_of_interest_computation = CharField(required=False)
    frequency_of_interest_crediting = CharField(required=False)
    days_in_a_year = IntegerField(initial=365)
    minimum_maintaining_balance = DecimalField(initial=0)
    # Credit related
    cut_off = IntegerField(required=False)

    branch = CharField()
    account_number = CharField()
    website = URLField()
    login_url = CharField()
