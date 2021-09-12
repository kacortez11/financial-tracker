from django.shortcuts import render

from .forms import ModeofPaymentForm
from .models import ModeOfPayment


def mode_of_payment_create_view(request):
	mop = ModeofPaymentForm(request.POST or None)
	if mop.is_valid():
		mop.save

	context = {
		'form': mop
	}

	return render(request, 'modeofpayment_create.html', context)


def mode_of_payment_detailed_view(request):
	expense = ModeOfPayment.objects.get(id=1)
	context = {
		'obj': expense
	}
	return render(request, 'modeofpayment_detail.html', context)
