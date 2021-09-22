from django.db.models import (
    Model,
    AutoField,
    DateTimeField, ForeignKey, PROTECT
)


class BaseModel(Model):
    id = AutoField(primary_key=True, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserModel(BaseModel):
    user = ForeignKey('users.User', PROTECT, null=False)

    class Meta:
        abstract = True
