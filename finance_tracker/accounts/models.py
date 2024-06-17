from django.db import models
from django.contrib.auth.models import User

class IncomeSource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    

    def __str__(self):
        return self.name
class ExpenseCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name
class Transaction(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSACTION_TYPES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, blank=True, null=True)
    source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.get_type_display()} - {self.amount}"

## budget/models.py
from django.db import models
from django.core.mail import send_mail

class Budget(models.Model):
    name = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    current_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def check_budget_overrun(self):
        if self.current_spent > self.limit:
            self.send_budget_overrun_notification()

    def send_budget_overrun_notification(self):
        send_mail(
            'Budget Overrun Alert',
            f'Your budget {self.name} has been overrun.',
            'from@example.com',
            [self.user.email],
            fail_silently=False,
        )
# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}"
    









