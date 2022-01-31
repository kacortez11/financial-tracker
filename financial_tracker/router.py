from rest_framework.routers import DefaultRouter

from api.categories.viewsets.category_viewset import CategoryViewSet
from api.categories.viewsets.courier_viewset import CourierViewSet
from api.categories.viewsets.location_viewset import LocationViewSet
from api.categories.viewsets.merchant_viewset import MerchantViewSet
from api.expenses.viewsets.expense_viewset import ExpenseViewSet
from api.expenses.viewsets.meal_viewset import MealViewSet
from api.incomes.viewset import IncomeViewSet
from api.invoices.viewset import InvoiceViewSet
from api.modes_of_payment.viewsets import ModeOfPaymentViewSet
from api.transfers.viewset import TransferViewSet
from api.users.viewsets.subscription_viewset import SubscriptionViewSet
from api.users.viewsets.person_viewset import PersonViewSet
from api.users.viewsets.user_viewset import UserViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('merchants', MerchantViewSet, basename='merchant')
router.register('locations', LocationViewSet, basename='location')
router.register('couriers', CourierViewSet, basename='courier')
router.register(
    'modes-of-payment',
    ModeOfPaymentViewSet,
    basename='mode-of-payment'
)
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('incomes', IncomeViewSet, basename='income')
router.register('invoices', InvoiceViewSet, basename='invoice')
router.register('transfers', TransferViewSet, basename='transfer')
router.register('users', UserViewSet, basename='user')
router.register('persons', PersonViewSet, basename='person')
router.register(
    'subscriptions',
    SubscriptionViewSet,
    basename='subscription'
)


router.register('meals', MealViewSet, basename='meal')
