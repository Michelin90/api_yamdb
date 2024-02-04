from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    CHOICES = [
        (USER, 'пользователь'),
        (MODERATOR, 'модератор'),
        (ADMIN, 'админ'),
    ]
    username = models.CharField(
        'Логин',
        unique=True,
        max_length=150,
        validators=[RegexValidator(regex=r'^[\w.@+-]+$')],
        db_index=True,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
        unique=True
    )
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
        max_length=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
