# budget/admin.py
from django.contrib import admin
from .models import Budget

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'category')

    def send_notification(self, request):
        # Your logic for sending notifications
        pass

admin.site.register(Budget, BudgetAdmin)


