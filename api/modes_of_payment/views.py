from django.shortcuts import render

from .forms import ModeofPaymentForm, RawModeOfPayment
from .models import ModeOfPayment


def create_view(request):  # Django Model Form
	mop = ModeofPaymentForm(request.POST or None)
	errors = None
	if mop.is_valid():
		mop.save()
		mop = ModeofPaymentForm() # rerender blank form
	else:
		errors = mop.errors

	context = {
		'form': mop,
		'errors': errors
	}

	return render(request, 'templates/create.html', context)


def raw_create_view(request):  # Raw Django Form
	mop = RawModeOfPayment()
	errors = None
	if request.method == 'POST':
		mop = RawModeOfPayment(request.POST or None)
		if mop.is_valid():
			ModeOfPayment.objects.create(**mop.cleaned_data)
			mop = ModeofPaymentForm()
		else:
			errors = mop.errors

	context = {
		'form': mop,
		'errors': errors
	}

	return render(request, 'templates/create_raw.html', context)


def detailed_view(request, mop_id):
	mop = ModeOfPayment.objects.get(id=mop_id)
	context = {
		'obj': mop
	}
	return render(request, 'templates/view_detailed.html', context)


def all_view(request):
	mop = ModeOfPayment.objects.all()
	context = {
		'obj': mop
	}
	return render(request, 'templates/view_all.html', context)
