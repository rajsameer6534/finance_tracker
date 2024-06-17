from django.shortcuts import render

# budget/views.py
from django.http import HttpResponse

def send_notification(request):
    # Your logic for sending notifications
    return HttpResponse("Notification sent.")

