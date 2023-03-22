from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    CHOICES = [
        (USER, 'пользователь'),
        (MODERATOR, 'модератор'),
        (ADMIN, 'админ'),
    ]
    email = models.EmailField(unique=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Право доступа',
        max_length=10,
        choices=CHOICES,
        default=USER,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
    )

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
