# Create your tests here.
from django.test import TestCase,Client,override_settings
from users.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import reverse

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class UserTestCase(TestCase):

    def setUp(self):
        # self.client = Client()
            self.u=User.objects.create_user(username="testuser",email="a@c.in",password="secret")
            self.p1=Profile.objects.create(user=self.u,bio="hello there",image="media/profile_pics/scene22.jpg")
            self.u2=User.objects.create_user(username="agar",password="secret23")

    def test_profile_model(self):
        self.assertEquals(Profile.objects.count(), 1)
        profile=Profile.objects.get(user_id=1)
        self.assertEquals(profile.image, "media/profile_pics/scene22.jpg")

    def test_profile_view(self):
        c=Client()
        response=c.get("/profile/edit/")
        self.assertEquals(self.p1.bio, "hello there")
        # updating bio
        self.p1.bio="Hello again"
        self.assertNotEquals(self.p1.bio, "hello there")

    def test_login(self):
        response= self.client.login(username='testuser',password='secret')
        self.assertEquals(response,True)
 
    

    


