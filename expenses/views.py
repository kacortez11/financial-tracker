from django.shortcuts import render

from .models import Expense


# Create your views here.
def expenses_detailed_view(request):
	expense = Expense.objects.get(id=1)
	context = {
		'obj': expense
	}
	return render(request, 'expense_detail.html', context)
