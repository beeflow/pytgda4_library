from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserQuerySet(UserManager):
    pass


class User(AbstractUser):
    card_number = models.CharField(
        verbose_name="Numer karty bibliotecznej",
        max_length=9, null=False, blank=False
    )

    objects = UserQuerySet()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.card_number:
            card_number = User.objects.count() + 1
            self.card_number = str(card_number).zfill(9)
        return super(User, self).save(*args, **kwargs)
