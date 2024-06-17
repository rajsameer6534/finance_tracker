from django.contrib import admin
from .models import IncomeSource, ExpenseCategory, Transaction

admin.site.register(IncomeSource)
admin.site.register(ExpenseCategory)
admin.site.register(Transaction)


from django.contrib import admin
from django.core.mail import send_mail
from.models import Budget

# budget/admin.py
from django.contrib import admin
from .models import Budget

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'limit', 'current_spent', 'user')

    def send_notification(self, request, queryset):
        for budget in queryset:
            # Trigger your notification logic here
            budget.check_budget_overrun()

    send_notification.short_description = 'Send notification for budget overruns'

admin.site.register(Budget, BudgetAdmin)

