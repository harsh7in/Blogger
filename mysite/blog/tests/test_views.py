from django.test import TestCase, Client, override_settings
from django.urls import reverse
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViews(TestCase):

    def setUp(self):
        self.u=User.objects.create_superuser(username="testuser",email="a@c.in",password="secret") # Create an User instance for performing the tests
        self.client = Client()

        # URL's of different view
        self.about_url = reverse('blog-about')
        self.viewcount_url = reverse('getBlogs')
        self.detailview_url = reverse('post-detail', args=['testblog1'])
        self.homeview_url = reverse('blog-home')
        self.profileview_url = reverse('blog-profile', args=[self.u.username])
        self.updateview_url = reverse('post-update', args=[1])
        self.postcreate_url = reverse('post_create')

        # Creating instances of the Model
        self.testblog1 = Post.objects.create(
            title       = 'testblog1',
            content     = 'This is only for testing purpose blog',
            author      = User.objects.get(email='a@c.in'),
            view_count  = 0,
        )
        self.testblog2 = Post.objects.create(
            title       = 'testblog2',
            content     = 'This is only for testing purpose blog',
            author      = User.objects.get(email='a@c.in'),
            view_count  = 0,
        )
        self.testblog3 = Post.objects.create(
            title       = 'testblog3',
            content     = 'This is only for testing purpose blog',
            author      = User.objects.get(email='a@c.in'),
            view_count  = 0,
        )
        self.testblog4 = Post.objects.create(
            title       = 'testblog4',
            content     = 'This is only for testing purpose blog',
            author      = User.objects.get(email='a@c.in'),
            view_count  = 0,
        )

    # Code for testing the `about` View
    def test_about_view_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    # Code for testing the `View Count feature` which uses Ajax Call
    def test_viewCount_GET(self):
        response = self.client.get(self.viewcount_url)
        self.assertEquals(response.status_code, 200)

    # Code for testing the `Post_Detail` view
    def test_postdetailView_GET(self):
        response = self.client.get(self.detailview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    # Code for testing the `Home` View
    def test_home_view_GET(self):
        response = self.client.get(self.homeview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    # Code for testing the `Profileview` View
    def test_profileview_GET(self):
        response = self.client.get(self.profileview_url)
        self.assertEquals(self.u.username, 'testuser')
        self.assertTemplateUsed(response, 'user/profile.html')

    # Code for testing the `postUpdatView` View
    def test_postupdateview_GET(self):
        self.testblog1.title = 'updating the title'
        self.assertNotEquals(self.testblog1.title, 'testblog1')

    # Code for testing the `post_create` View
    # def testpostcreateview_GET(self):
    #     self.client.login(username='testuser', password='secret')
    #     # self.tusu = Post.objects.create(title= 'this created by the client',content='this is the content of the blog-post')    
    #     print(Post.objects.all().count())
    #     # self.assertEquals()
    #     # self.assertEquals(response, True)
