from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    as_client = models.BooleanField(default=False)
    as_consultant = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

    """user model"""

class profil_consultant(models.Model):
    user=models.OneToOneField(User,related_name='consultant' , on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    expertise_field = models.CharField(max_length=50,null=True)
    statment = models.TextField(max_length=240,null=True)
    image = models.ImageField(upload_to="images/",null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    """ model for create profile consultant"""

class profil_client(models.Model):
    user = models.OneToOneField(User, related_name='client' , on_delete=models.CASCADE)
    age = models.IntegerField(null=True)

""" model for create profile client"""

