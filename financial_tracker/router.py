from rest_framework.routers import DefaultRouter

from categories.viewsets import CategoryViewSet
from users.viewsets import UserViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('expenses', CategoryViewSet, basename='expense')
router.register('incomes', CategoryViewSet, basename='income')
router.register('invoices', CategoryViewSet, basename='invoice')
router.register('transfers', CategoryViewSet, basename='transfer')
router.register('users', UserViewSet, basename='user')
