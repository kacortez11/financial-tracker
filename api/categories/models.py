from django.db.models import (
    CharField, BooleanField, ForeignKey, PROTECT,
    UniqueConstraint, FloatField,
)

from api.core.models import BaseModel, BaseUserModel


class Category(BaseUserModel):
    EXPENSES = 'expense'
    INCOME = 'income'
    TRANSFER = 'transfer'
    TRANSACTION_TYPES = (
        (EXPENSES, EXPENSES),
        (INCOME, INCOME),
        (TRANSFER, TRANSFER)
    )

    transaction_type = CharField(
        max_length=8,
        choices=TRANSACTION_TYPES,
        blank=False
    )
    category = CharField(max_length=32, null=False)
    description = CharField(max_length=128, blank=True, null=True)
    has_subcategory = BooleanField(default=False)
    parent = ForeignKey(
        'categories.Category',
        PROTECT,
        related_name='category_parent',
        null=True
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'category'],
                name='unique_user_category'
            ),
            UniqueConstraint(
                fields=['parent', 'category'],
                name='unique_parent_child_category'
            ),
        ]

    def __str__(self):
        return self.category.capitalize()


class Merchant(BaseUserModel):
    merchant = CharField(max_length=64, blank=False)
    category = ForeignKey(  # meal restaurants, grocery, adulting, whatevz
        'categories.Category',
        PROTECT,
        related_name='merchant_category',
        null=False
    )

    def __str__(self):
        return self.merchant


class Location(BaseUserModel):
    category = ForeignKey(  # transpo
        'categories.Category',
        PROTECT,
        related_name='destination_category',
        null=False
    )
    value = CharField(max_length=32, blank=False)
    longitude = FloatField(null=True)
    latitude = FloatField(null=True)

    def __str__(self):
        return self.value.capitalize()


class Courier(BaseUserModel):
    category = ForeignKey(  # online shopping
        'categories.Category',
        PROTECT,
        related_name='courier_category',
        null=False
    )
    value = CharField(max_length=32, blank=False)

    def __str__(self):
        return self.value.capitalize()
