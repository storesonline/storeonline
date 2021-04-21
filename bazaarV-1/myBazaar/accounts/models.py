from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    cell = models.CharField(max_length=20, default='+92 xxx xxxxxxx', null=True, blank=True)


