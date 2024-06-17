from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    # Code for login view will go here
    pass

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import IncomeSource, ExpenseCategory, Transaction
from .forms import IncomeSourceForm, ExpenseCategoryForm, TransactionForm

@login_required
def add_income_source(request):
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            income_source = form.save(commit=False)
            income_source.user = request.user
            income_source.save()
            return redirect('profile')
    else:
        form = IncomeSourceForm()
    return render(request, 'accounts/add_income_source.html', {'form': form})

@login_required
def add_expense_category(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense_category = form.save(commit=False)
            expense_category.user = request.user
            expense_category.save()
            return redirect('profile')
    else:
        form = ExpenseCategoryForm()
    return render(request, 'accounts/add_expense_category.html', {'form': form})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('profile')
    else:
        form = TransactionForm()
    return render(request, 'accounts/add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'accounts/edit_transaction.html', {'form': form})

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('profile')
    return render(request, 'accounts/delete_transaction.html', {'transaction': transaction})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction
import json

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    # Prepare data for charts
    income = transactions.filter(type='IN').values('date', 'amount')
    expenses = transactions.filter(type='EX').values('date', 'amount')

    # Convert queryset to list for JSON serialization
    income_data = {
        'labels': [str(data['date']) for data in income],
        'data': [float(data['amount']) for data in income],
    }

    expenses_data = {
        'labels': [str(data['date']) for data in expenses],
        'data': [float(data['amount']) for data in expenses],
    }

    context = {
        'income_data': json.dumps(income_data),
        'expenses_data': json.dumps(expenses_data),
    }

    return render(request, 'accounts/dashboard.html', context)
from django.db.models import Sum
from django.utils import timezone

@login_required
def report(request):
    # Get today's date and start of the current month
    today = timezone.now().date()
    start_of_month = today.replace(day=1)
    
    # Filter transactions for the logged-in user from the start of the current month
    transactions = Transaction.objects.filter(user=request.user, date__gte=start_of_month)
    
    # Calculate total income, expenses, and savings
    income = transactions.filter(type='IN').aggregate(total_income=Sum('amount'))['total_income'] or 0
    expenses = transactions.filter(type='EX').aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0
    savings = income - expenses

    context = {
        'income': income,
        'expenses': expenses,
        'savings': savings,
    }

    return render(request, 'accounts/report.html', context)
# views.py or wherever your budget check logic resides

# accounts/views.py
from django.shortcuts import render
from .models import Notification

def send_notification(request):
    # Your logic to send notification
    # Example: Create a notification
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message')
        Notification.objects.create(user=user, message=message)
        return render(request, 'notification_sent.html')
    return render(request, 'send_notification.html')








@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})
