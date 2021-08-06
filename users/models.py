from django.db.models import CharField

from core.models import BaseModel


class User(BaseModel):
    username = CharField(max_length=16, blank=False, null=False)
