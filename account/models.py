from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    patronymic = models.CharField(max_length=20)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now=True)
