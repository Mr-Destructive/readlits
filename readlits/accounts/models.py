from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
