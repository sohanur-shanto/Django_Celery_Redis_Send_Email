from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail('Celery Working', 'Celery is cool I guess',
    "sohanur.shanto@northsouth.edu",
    ['laksura.com.bd@gmail.com'],
    fail_silently=True)
    return None
