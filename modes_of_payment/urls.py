from django.contrib import admin
from django.urls import path

from modes_of_payment.views import (
    create_view,
    raw_create_view,
    all_view,
    detailed_view
)

urlpatterns = [
    path('modes_of_payment/all', all_view),
    path('modes_of_payment/<int:mop_id>', detailed_view),
    path('modes_of_payment/create', create_view),
    path('modes_of_payment/create_raw', raw_create_view),
]
