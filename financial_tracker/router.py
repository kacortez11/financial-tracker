from rest_framework.routers import DefaultRouter

from categories.viewsets.category_viewset import CategoryViewSet
from categories.viewsets.courier_viewset import CourierViewSet
from categories.viewsets.location_viewset import LocationViewSet
from categories.viewsets.merchant_viewset import MerchantViewSet
from modes_of_payment.viewsets import ModeOfPaymentViewSet
from transfers.viewset import TransferViewSet
from users.viewsets.subscription_viewset import SubscriptionViewSet
from users.viewsets.person_viewset import PersonViewSet
from users.viewsets.user_viewset import UserViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('merchant', MerchantViewSet, basename='merchant')
router.register('location', LocationViewSet, basename='location')
router.register('courier', CourierViewSet, basename='courier')
router.register(
    'modes-of-payment',
    ModeOfPaymentViewSet,
    basename='mode-of-payment'
)
router.register('expenses', CategoryViewSet, basename='expense')
router.register('incomes', CategoryViewSet, basename='income')
router.register('invoices', CategoryViewSet, basename='invoice')
router.register('transfers', TransferViewSet, basename='transfer')
router.register('users', UserViewSet, basename='user')
router.register('persons', PersonViewSet, basename='person')
router.register('subscriptions', SubscriptionViewSet, basename='subscription')
