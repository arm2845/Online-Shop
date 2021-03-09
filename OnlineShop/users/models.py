from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="profile_images", default="image.png")

    def __str__(self):
        return f"{self.user} {self.surname}"
