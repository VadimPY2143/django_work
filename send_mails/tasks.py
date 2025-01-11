from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from PIL import Image


@shared_task
def send_email_task(from_email, subject, message, recipient_list):
    send_mail(subject,message,from_email, recipient_list)
    return True


@shared_task
def send_email_task_html(subject: str, html_message: str, recipient_list: list, from_email: str):
    email = EmailMultiAlternatives(subject=subject,
                                   body=html_message,
                                   from_email=from_email,
                                   to=[recipient_list])

    email.attach_alternative(html_message, "text/html")
    email.send(fail_silently=False)
    return True


@shared_task
def compress_image_task(image_path, output_path, quality=20):
    img = Image.open(image_path)
    img.save(image_path, optimize=True, quality=quality)
    return f'Image compressed successfully and saved at {output_path}'

