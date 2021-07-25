from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'profiles/')
  bio = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=CASCADE)
  admin = models.BooleanField()

  def save_profile(self):
    self.save()

  @classmethod
  def update_profile(cls, id, bio):
    to_update = cls.objects.filter(id = id)
    to_update.update(bio = bio)

class Neighbourhood(models.Model):
  name = models.CharField(max_length=250)
  location = models.TextField()
  population = models.IntegerField()
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)

