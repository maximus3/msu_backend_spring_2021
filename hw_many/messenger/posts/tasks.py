from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_email_if_new_object(title):
    send_mail(
        "New post created",
        f"New post {title} created",
        "max2000.gym5cheb@gmail.com",
        ["max2000.gym5cheb@yandex.ru"],
        fail_silently=True,
    )
    print('Email sended')  # TODO
