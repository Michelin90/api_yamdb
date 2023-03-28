import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from reviews.models import User


def code_to_email(user):
    random.seed()
    user = get_object_or_404(
        User, username=user
    )
    confirmation_code = str(random.randint(10000, 99999))
    user.confirmation_code = confirmation_code
    user.save()
    send_mail(
        subject='Код подтверждения',
        message=confirmation_code,
        recipient_list=[user.email],
        from_email=settings.EMAIL_HOST_USER,
        fail_silently=False,
    )
