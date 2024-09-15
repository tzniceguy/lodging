from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    USER_ROLES = [
        ('Customer', 'Customer'),
        ('Owner', 'Owner'),
        ('Admin', 'Admin'),
    ]
    user_role = models.CharField(max_length=20, choices=USER_ROLES)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)



class Lodge(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lodges')
    lodge_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    description = models.TextField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lodge_name
