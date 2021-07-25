from typing import NewType
from hoodalert.models import Business, HealthDep, Neighbourhood, PoliceDep, Posts, UserProfile, User
from django.test import TestCase

# Create your tests here.
class TestPoliceDep(TestCase):
  def setUp(self):
    self.new_pd = PoliceDep(1, 'temp pd', '911', '911@gmail.com')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_pd, PoliceDep))

  def test_create_pd(self):
    PoliceDep.create_pd('holy pd', '999', '999@gmail.com')
    pds = PoliceDep.objects.all()

    self.assertTrue(len(pds)>0)


class TestPoliceDep(TestCase):
  def setUp(self):
    self.new_hd = HealthDep(1, 'temp hd', '411', '411@gmail.com')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_hd, HealthDep))

  def test_create_hd(self):
    HealthDep.create_hd('holy hd', '990', '990@gmail.com')
    hds = HealthDep.objects.all()

    self.assertTrue(len(hds)>0)

# class TestUserProfile(TestCase):
#   def setUp(self):
#     self.new_pd = PoliceDep(name = 'temp pd', contact = '911', email = '911@gmail.com')
#     self.new_hd = HealthDep(name = 'temp hd', contact = '411', email = '411@gmail.com')
#     self.new_pd.save
#     self.new_hd.save
#     pd = PoliceDep.objects.get(pk = 1)
#     hd = HealthDep.objects.get(pk = 1)
#     self.new_hood = Neighbourhood(name = 'Karuturi', location = '1st Avenue', population = 200233 ,police_dep = self.new_pd, health_dep = self.new_hd)
#     self.new_hood.save()
#     self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
#     self.new_user.save()
#     self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg','live love laugh','peacefule and communal','f', self.new_neighborhood, self.new_user)

#   def test_instance(self):
#     self.assertTrue(isinstance(self.new_profile, UserProfile))

#   def test_saveuserprofile(self):
#     self.new_profile.save_profile()
#     profiles = UserProfile.objects.all()

#     self.assertEqual(len(profiles), 1)

  # def test_update_user_profile(self):
  #   self.new_profile.save_profile()
  #   user = User.objects.get(pk = 1)
  #   new_bio = 'make sun'
  #   UserProfile.update_profile(1, new_bio)
  #   uptodate = UserProfile.objects.get(pk = 1)
  #   uptodate.refresh_from_db()

  #   self.assertEqual(uptodate.bio, new_bio)

# class TestNeighbourhood(TestCase):
#   def setUp(self):
#     self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
#     self.new_user.save()
#     self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'peacefule and communal',1, 'live love laugh',1,'t')
#     self.new_profile.save_profile()
#     self.new_neighborhood = Neighbourhood(name = 'Karuturi', location = '1st Avenue', population = 200233 ,police_dep = self.new_pd, health_dep = self.new_hd)

#   def test_instance(self):
#     self.assertTrue(isinstance(self.new_neighborhood, Neighbourhood))

#   def test_create_neighbourhood(self):
#     Neighbourhood.create_hood('Albionz', 'junction road', 23334, self.new_profile)
#     hoods = Neighbourhood.objects.all()
#     self.assertEqual(len(hoods), 1)
  
#   def test_delete_neighbourhood(self):
#     self.new_neighborhood.save()
#     self.new_neighborhood.delete_neighbourhood()
#     hoods = Neighbourhood.objects.all()

#     self.assertEqual(len(hoods), 0)

#   def test_find_neighbourhood(self):
#     self.new_neighborhood.save()
#     found_hood = Neighbourhood.find_hood('Karuturi')

#     self.assertTrue(found_hood.name,'Karuturi')

#   def test_update_occupants(self):
#     self.new_neighborhood.save()
#     updated = Neighbourhood.update_occupants('Karuturi', 2345)
#     self.assertEqual(updated.population, 2345)

#   def test_update_neighbourhood(self):
#     self.new_neighborhood.save()
#     updated = Neighbourhood.update_neighborhood('Karuturi','Aston', '2nd Avenue')

#     self.assertEqual((updated.name,updated.location),('Aston', '2nd Avenue'))

class TestBusiness(TestCase):
  def setUp(self):
    self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
    self.new_user.save()

    new_hd = HealthDep(1,'holy hd', '990', '990@gmail.com')
    new_hd.save()
    new_pd = PoliceDep(1,'holy pd', '999', '999@gmail.com')
    new_pd.save()   

    self.new_neighborhood = Neighbourhood(1,'Karuturi', '1st Avenue',200233, 1, 1)
    self.new_neighborhood.save()
    self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'peacefule and communal', 'live love laugh','f',1,1)
    self.new_profile.save_profile()
    self.new_business = Business(1, 'Coffee Shop', 'coffee@gmail.com','junctionroad', 1, 1)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_business, Business))


  def test_create_business(self):
    usr_prof = UserProfile.objects.get(pk = 1)
    hood = Neighbourhood.objects.get(pk = 1)
    Business.create_business('Coffee Shop', 'coffee@gmail.com','junctionroad', usr_prof, hood)
    businesses = Neighbourhood.objects.all()
    
    self.assertEqual(len(businesses), 1)

  def test_delete_business(self):
    self.new_business.save()
    self.new_business.delete_business()
    businesses = Business.objects.all()

    self.assertEqual(len(businesses), 0)

  def test_find_business(self):
    self.new_business.save()
    found_business = Business.find_business('Coffee Shop')

    self.assertTrue(found_business.name,'Coffee Shop')
  
  def test_update_business(self):
    self.new_business.save()
    updated = Business.update_business('Coffee Shop', 'Cyber Shop','email@gmail.com', '2nd Avenue')

    self.assertEqual((updated.name, updated.email, updated.location),('Cyber Shop', 'email@gmail.com', '2nd Avenue'))

# class TestPosts(TestCase):
#   def setUp(self):
#     self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'peacefule and communal',1, 'live love laugh',1,'t')
#     self.new_profile.save_profile()
#     self.new_post = Posts('what a day', 'so today statted', self.new_profile, 'image' )

#   def test_instance(self):
#     self.assertTrue(isinstance(self.new_post, Posts))
  