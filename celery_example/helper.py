from django.core.mail import send_mail

def send_mail_without_task():
    send_mail('Celery Working', 'Celery is cool I guess',
    "sohanur.shanto@northsouth.edu",
    ['laksura.com.bd@gmail.com'],
    fail_silently=True)
    return None