from hoodalert.models import Neighbourhood, UserProfile, User
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
    self.save_profile()
    slef.new_neighborhood = Neighbourhood()

