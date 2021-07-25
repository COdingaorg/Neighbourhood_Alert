from hoodalert.models import Business, Neighbourhood, UserProfile, User
from django.test import TestCase

# Create your tests here.
class TestUserProfile(TestCase):
  def setUp(self):
    self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
    self.new_user.save()
    self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'live love laugh',1)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_user, User))
    self.assertTrue(isinstance(self.new_profile, UserProfile))

  def test_saveuserprofile(self):
    self.new_profile.save_profile()
    profiles = UserProfile.objects.all()

    self.assertEqual(len(profiles), 1)

  def test_update_user_profile(self):
    self.new_profile.save_profile()
    user = User.objects.get(pk = 1)
    new_bio = 'make sun'
    UserProfile.update_profile(1, new_bio)
    uptodate = UserProfile.objects.get(pk = 1)
    uptodate.refresh_from_db()

    self.assertEqual(uptodate.bio, new_bio)

class TestNeighbourhood(TestCase):
  def setUp(self):
    self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
    self.new_user.save()
    self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'live love laugh',1)
    self.new_profile.save_profile()
    self.new_neighborhood = Neighbourhood(name = 'Karuturi', location = '1st Avenue', population = 200233 , admin_user_prof = self.new_profile)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_neighborhood, Neighbourhood))

  def test_create_neighbourhood(self):
    Neighbourhood.create_hood('Albionz', 'junction road', 23334, self.new_profile)
    hoods = Neighbourhood.objects.all()
    self.assertEqual(len(hoods), 1)
  
  def test_delete_neighbourhood(self):
    self.new_neighborhood.save()
    self.new_neighborhood.delete_neighbourhood()
    hoods = Neighbourhood.objects.all()

    self.assertEqual(len(hoods), 0)

  def test_find_neighbourhood(self):
    self.new_neighborhood.save()
    found_hood = Neighbourhood.find_hood('Karuturi')

    self.assertTrue(found_hood.name,'Karuturi')

  def test_update_occupants(self):
    self.new_neighborhood.save()
    updated = Neighbourhood.update_occupants('Karuturi', 2345)
    self.assertEqual(updated.population, 2345)

  def test_update_neighbourhood(self):
    self.new_neighborhood.save()
    updated = Neighbourhood.update_neighborhood('Karuturi','Aston', '2nd Avenue')

    self.assertEqual((updated.name,updated.location),('Aston', '2nd Avenue'))

class TestBusiness(TestCase):
  def setUp(self):
    self.new_user = User(1, 'pbkdf2_sha256$260000$NjKSHSB0A7GnXFtsT4LF3E$OtsaM4UTtddrKX81NiyU45bnVt8BOZLzHYHQP5D/fkw=','2021-07-25 00:44:38.631522+03', 'f' , 'codinga', 'caleb', 'odinga','calemasanga@gmail.com','f','t','2021-07-24 23:41:50.483079+03')
    self.new_user.save()
    self.new_profile = UserProfile(1, 'profiles/girl-cg-artwork-anime-art-anime-girl-wallpaper-preview.jpg', 'live love laugh',1)
    self.new_profile.save_profile()
    self.new_neighborhood = Neighbourhood(name = 'Karuturi', location = '1st Avenue', population = 200233 , admin_user_prof = self.new_profile)
    self.new_neighborhood.save()
    self.new_business = Business(name = 'Coffee Shop', email = 'coffee@gmail.com', user_prof=self.new_profile, neighborhood = self.new_neighborhood)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_business, Business))

  def test_create_business(self):
    Business.create_business('coffee shop', 'email@gmail.com', 'junction road',self.new_profile, self.new_neighborhood)
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

  