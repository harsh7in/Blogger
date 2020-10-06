from django.test import TestCase, Client, override_settings
from django.urls import reverse
from blog.models import Post

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.about_url = reverse('blog-about')
        self.viewcount_url = reverse('getBlogs')
        # self.detailview_url = reverse('post-detail', args=['letsfghj'])
        # self.home_url = reverse('blog-home')


    def test_about_view_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_viewCount_GET(self):
        response = self.client.get(self.viewcount_url)
        self.assertEquals(response.status_code, 200)

    # def test_postdetailView_GET(self):
    #     response = self.client.get(self.detailview_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_detail.html')

    # def test_home_view_GET(self):
    #     response = self.client.get(self.home_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/.html')












# Name of the View functions

# 4. Profileview []
# 5. PostDetail []
# 6. PostUpdateView []
# 7. PostDeleteView []
# 8. post_create []





# 2. home [Simple]


# After all the tests scripts are written order them according to the order of their view function in view.py file