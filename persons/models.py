from django.db.models import ForeignKey, PROTECT, CharField

from core.models import BaseUserModel


class Person(BaseUserModel):
    user = ForeignKey('users.User', PROTECT, null=False)
    first_name = CharField(max_length=16, blank=False, null=False)
    last_name = CharField(max_length=16, blank=False, null=False)
    display_name = CharField(max_length=16, null=True)
