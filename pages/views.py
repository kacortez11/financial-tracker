from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")


def about_view(request, *args, **kwargs):
	my_context = {
		'request': request,
		'my_context': 'This is about us',
		'my_number': 123,
		'my_list': [123, 4324, 54343],
	}
	return render(request, 'about.html', my_context)

