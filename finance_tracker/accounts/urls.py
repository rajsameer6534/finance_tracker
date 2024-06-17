from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('add_income_source/', views.add_income_source, name='add_income_source'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_income_source/', views.add_income_source, name='add_income_source'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('add_income_source/', views.add_income_source, name='add_income_source'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('send-notification/', views.send_notification, name='send_notification'),
     
]



