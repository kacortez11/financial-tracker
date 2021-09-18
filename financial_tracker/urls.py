"""financial_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, contact_view
from expenses.views import expenses_detailed_view
from modes_of_payment.views import (
    create_view,
    raw_create_view,
    all_view,
    detailed_view
)
from categories.views import (
    create_category,
    get_categories,
    get_category_by_id
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('about', about_view),
    path('contact', contact_view),
    path('expense/', expenses_detailed_view),

    path('categories', get_categories),
    path('categories/<int:category_id>', get_category_by_id),
    path('categories/create', create_category),

    path('modes_of_payment/all', all_view),
    path('modes_of_payment/<int:mop_id>', detailed_view),
    path('modes_of_payment/create', create_view),
    path('modes_of_payment/create_raw', raw_create_view),
]
