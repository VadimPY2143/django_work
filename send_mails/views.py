from django.http import JsonResponse
from send_mails.tasks import send_email_task, send_email_task_html
from dotenv import load_dotenv
import os
from django.template.loader import render_to_string
from django.utils.html import strip_tags

load_dotenv()


def send_mail_view(request):
    subject = 'Test Email'
    message = 'This is a test email.'
    from_email = os.getenv('EMAIL_HOST_USER')
    recipient_list = ['vadimpapusha2310@gmail.com']
    send_email_task.delay(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    return JsonResponse({'status': 'success'})


def send_email_html(request):
    subject = 'Test Email'
    message = render_to_string('email_message.html')

    send_email_task_html.delay(
        subject=subject,
        message=message,
        recepient_list=['vadimpapusha2310@gmail.com']
    )
    return JsonResponse({'status': 'success'})
