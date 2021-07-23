from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, relate_name="profile")

    image = models.imageField(upload_to='profile/', null=True)
    nickname = models.charField(max_length = 20, unique=True, null=True)
    message = models.CharField(max_length = 100, null=True)
