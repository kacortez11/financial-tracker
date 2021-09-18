from django.shortcuts import render

from .forms import CategoryForm
from .models import Category


def create_category(request):  # Django Model Form
	mop = CategoryForm(request.POST or None)
	errors = None
	if mop.is_valid():
		mop.save()
		mop = CategoryForm() # rerender blank form
	else:
		errors = mop.errors

	context = {
		'form': mop,
		'errors': errors
	}

	return render(request, 'create.html', context)


def get_category_by_id(request, category_id=None):
	
	mop = Category.objects.get(id=category_id)
	context = {
		'obj': mop
	}
	return render(request, 'view_detailed.html', context)


def get_categories(request):
	mop = Category.objects.all()
	context = {
		'obj': mop
	}
	return render(request, 'view_all.html', context)
