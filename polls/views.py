from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def index(request):
    send_mail('Subject here', 'Here is the message.', 'ramya.gangula@microsoft.com', ['ramya.gangula@microsoft.com'], fail_silently=False)
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
