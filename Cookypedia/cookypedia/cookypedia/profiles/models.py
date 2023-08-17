from django.db import models
from django.contrib.auth import models as auth_models


class CustomUser(auth_models.AbstractUser):
    profile_image = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
