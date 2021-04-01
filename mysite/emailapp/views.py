from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def subscribe(request):
    subject = 'Subject here'
    message = 'Here is the message.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['davidpoarch@outlook.com']
    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)

    return HttpResponse("Email sent successfully!")
