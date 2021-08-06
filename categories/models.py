from django.db.models import CharField, BooleanField, ForeignKey, PROTECT, JSONField, UniqueConstraint

from core.models import BaseModel, BaseUserModel


class Category(BaseUserModel):
	EXPENSES = 'expense'
	INCOME = 'income'
	TRANSACTION_TYPES = (
		(EXPENSES, EXPENSES),
		(INCOME, INCOME)
	)

	transaction_type = CharField(max_length=16, choices=TRANSACTION_TYPES, blank=False)
	category = CharField(max_length=32, blank=False)
	label = CharField(max_length=64, blank=False)
	has_subcategory = BooleanField(default=False)
	parent_id = ForeignKey('categories.Category', PROTECT, related_name='category_parent_id', null=True)
	user_id = ForeignKey('users.User', PROTECT, related_name='user_id', null=True)
	history = JSONField()

	class Meta:
		constraints = [
			UniqueConstraint(fields=['user_id', 'category'], name='unique_user_category'),
			UniqueConstraint(fields=['parent_id', 'category'], name='unique_parent_child_category'),
		]
