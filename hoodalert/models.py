from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.forms.models import model_to_dict, modelformset_factory

# Create your models here.
class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'profiles/')
  bio = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=CASCADE)
  is_admin = models.BooleanField(default=False)

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
  admin_user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)

  @classmethod
  def create_hood(cls, name, location, population, user_profile):
    new_hood = cls(name = name, location = location, population = population, admin_user_prof = user_profile)
    new_hood.save()

  @classmethod
  def delete_hood(cls, id):
    to_delete = cls.objects.get(id = id)
    to_delete.delete()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def find_hood(cls, name):
    to_find = cls.objects.get(name = name)
    return to_find

class Admin(models.Model):
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)  

class Business(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)

