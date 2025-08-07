from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_application_notification(employer_email, seeker_email, job_title):
    subject = f"New Application for {job_title}"
    message = f"You have received a new application from {seeker_email}."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [employer_email]
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def print_hello():
    print("Hello World!")
