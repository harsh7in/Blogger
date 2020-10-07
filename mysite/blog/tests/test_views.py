from django.test import TestCase, Client, override_settings
from django.urls import reverse
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViews(TestCase):

    def setUp(self):
        self.u=User.objects.create_user(username="testuser",email="a@c.in",password="secret") # Create an User instance for performing the tests
        self.client = Client()

        # URL's of different view
        self.about_url = reverse('blog-about')
        self.viewcount_url = reverse('getBlogs')
        self.detailview_url = reverse('post-detail', args=['testblog1'])
        self.homeview_url = reverse('blog-home')
        self.deleteview_url = reverse('post-delete', args=[1])

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

    # Code for testing the `PostDelete` View [class based view]
    # def test_postdelete_view_GET(self):
    #     deletepost1 = Post.objects.create(
    #         title       = 'testblogfordelte',
    #         content     = 'This is only for testing purpose blog',
    #         author      = User.objects.get(email='a@c.in'),
    #         view_count  = 0,
    #     )
    #     deletepost1.delete()
    #     response = self.client.delete(self.deleteview_url)
    #     self.assertEquals(response.status_code, 204)










# Name of the View functions



# 4. Profileview []
# 6. PostUpdateView []

# 8. post_create []




# 7. PostDeleteView []



# After all the tests scripts are written order them according to the order of their view function in view.py file