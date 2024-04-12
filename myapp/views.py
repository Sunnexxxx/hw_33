from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import User


def send_password_reset_emails(users):
    for user in users:
        subject = 'Сброс пароля'
        message = 'Здравствуйте, {}. Для сброса пароля перейдите по ссылке: {}'.format(user.username, user.password_reset_link)
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])


def send_password_reset_request(request):
    users_needing_reset = User.objects.filter(needs_password_reset=True)
    send_password_reset_emails(users_needing_reset)
    return render(request, 'password_reset_sent.html')

