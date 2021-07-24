from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'profiles/')
  bio = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=CASCADE)
  