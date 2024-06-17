from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Split
from django.contrib.auth.models import User

@login_required
def create_expense(request):
    if request.method == 'POST':
        description = request.POST['description']
        total_amount = request.POST['total_amount']
        users = request.POST.getlist('users')
        
        expense = Expense.objects.create(
            description=description,
            total_amount=total_amount,
            created_by=request.user
        )

        split_amount = float(total_amount) / len(users)
        for user_id in users:
            user = User.objects.get(id=user_id)
            Split.objects.create(expense=expense, user=user, amount_owed=split_amount)

        return redirect('expense_list')
    
    users = User.objects.all()
    return render(request, 'split_expenses/create_expense.html', {'users': users})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(created_by=request.user)
    return render(request, 'split_expenses/expense_list.html', {'expenses': expenses})
