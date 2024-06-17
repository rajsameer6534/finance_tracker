from django.urls import path
from .views import create_expense, expense_list
app_name = 'split_expenses'  # Add this line for namespacing

urlpatterns = [
    path('create/', create_expense, name='create_expense'),
    path('list/', expense_list, name='expense_list'),
]
