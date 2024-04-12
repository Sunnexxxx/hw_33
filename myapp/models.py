from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    needs_password_reset = models.BooleanField(default=True)

