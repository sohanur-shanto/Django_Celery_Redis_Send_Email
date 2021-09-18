from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from django.core.mail import send_mail
from .helper import *


def index(request):
    send_mail_task.delay()
    return HttpResponse("hello")



