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
  name = models.CharField(max_length=250, unique=True)
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

  @classmethod
  def update_occupants(cls, name, new_population):
    cls.objects.filter(name = name).update(population = new_population)
    updated = cls.objects.get(name = name)
    return updated

  @classmethod
  def update_neighborhood(cls,old_name, new_name, new_location ):
    cls.objects.filter(name = old_name).update(name = new_name, location = new_location)
    updated = cls.objects.get(name = new_name)
    return updated


class Admin(models.Model):
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)  

class Business(models.Model):
  name = models.CharField(max_length=200, unique=True)
  email = models.EmailField()
  location = models.TextField()
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)

  @classmethod
  def create_business(cls, name, email, location, user_profile, neighbourhood ):
    new_hood = cls(name = name, email = email, location = location, user_prof = user_profile, neighborhood = neighbourhood)
    new_hood.save()
  
  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    to_find = cls.objects.get(name = name)
    return to_find
