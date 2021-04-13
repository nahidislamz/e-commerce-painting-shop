from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    about = models.TextField(null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.TextField()
    logo = models.ImageField(default="profile.jpg", null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
