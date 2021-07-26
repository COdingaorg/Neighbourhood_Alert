from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class PoliceDep(models.Model):
  name = models.CharField(max_length=250)
  contact = models.CharField(max_length=15)
  email = models.EmailField()

  def __str__(self):
    return self.name

  @classmethod
  def create_pd(cls, name, contact, email):
    new_pd = cls(name = name, contact = contact, email = email)
    new_pd.save()

class HealthDep(models.Model):
  name = models.CharField(max_length=250)
  contact = models.CharField(max_length=15)
  email = models.EmailField()

  def __str__(self):
    return self.name

  @classmethod
  def create_hd(cls, name, contact, email):
    new_hd = cls(name = name, contact = contact, email = email)
    new_hd.save()

class Neighbourhood(models.Model):
  name = models.CharField(max_length=250, unique=True)
  location = models.TextField()
  population = models.IntegerField()
  police_dep = models.ForeignKey(PoliceDep, on_delete=CASCADE, null=True)
  health_dep = models.ForeignKey(HealthDep, on_delete=CASCADE, null=True)

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

# Create your models here.
class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'profiles/')
  about = models.CharField(max_length=200)
  location_description = models.TextField(null=True)
  is_admin = models.BooleanField(default=False)
  hood = models.ForeignKey(Neighbourhood, on_delete=CASCADE, null=True)
  user = models.ForeignKey(User, on_delete=CASCADE)


  def save_profile(self):
    self.save()

  @classmethod
  def update_profile(cls, id, about):
    to_update = cls.objects.filter(id = id)
    to_update.update(about = about)

  @classmethod
  def get_user_profile(cls, user):
    user_profile = cls.objects.filter(user = user).last()
    return user_profile

class Admin(models.Model):
  user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)  

class Business(models.Model):
  name = models.CharField(max_length=200, unique=True)
  email = models.EmailField()
  location_or_Description = models.TextField()
  owner_user_prof = models.ForeignKey(UserProfile, on_delete=CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood, on_delete=CASCADE)

  @classmethod
  def create_business(cls, name, email, location, user_profile_id, neighbourhood_id ):
    new_hood = cls(name = name, email = email, location_or_Description = location, owner_user_prof = user_profile_id, neighborhood = neighbourhood_id)
    new_hood.save()
  
  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    to_find = cls.objects.get(name = name)
    return to_find

  @classmethod
  def update_business(cls,old_name, new_name, new_email, new_location ):
    cls.objects.filter(name = old_name).update(name = new_name, email = new_email, location_or_Description = new_location)
    updated = cls.objects.get(name = new_name)
    return updated

class Posts(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  post_image = models.ImageField(upload_to = 'posts/')
  poster = models.ForeignKey(UserProfile, on_delete=CASCADE)
  date_created = models.DateTimeField(null=True)
  class Meta:
    ordering = ['-id']
  

  def __str__(self):
    return self.title

  @classmethod
  def create_post(cls, name, title, description):
    pass


  

