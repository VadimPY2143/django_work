from django.urls import path
from .views import send_mail_view, send_email_html
urlpatterns = [
    path('send_mail/', send_mail_view, name='send_mail'),
    path('send_email_html/', send_email_html, name='send_email_html'),
]