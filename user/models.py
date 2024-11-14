from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель пользователя с добавлением поля email
class CustomUser(AbstractUser):                         # кастомную модель пользователя
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email'            # поле для входа
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email