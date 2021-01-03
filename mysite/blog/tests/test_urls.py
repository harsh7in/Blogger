from django.test import TestCase
from django.urls import reverse, resolve
from blog.models import Post
import blog.views
from blog.tests.test_views import TestViews

# unit tests for functions in urls.py
class TestUrls(TestCase):

# Code for testing home url
	def test_home(self):
		url=reverse('blog-home')
		self.assertEquals(url,'/')

# Code for testing about url
	def test_about(self):
		url=reverse('blog-about')
		self.assertEquals(url,'/about/')

# Code for testing getBlogs url
	def test_getblogs(self):
		url=reverse('getBlogs')
		self.assertEquals(url,'/ajax/getBlogs')

# Code for testing post create url
	def test_post_create(self):
		url=reverse('post_create')
		self.assertEquals(url,'/post_create/')

# Code for testing post detail url
	def test_blogdetail(self):
		url=reverse('post-detail',args=['testblog1'])
		self.assertEquals(url,'/post/testblog1/')

# Code for testing like toggle url
	def test_blogpost_like(self):
		url=reverse('like-toggle',args=['testblog1'])
		self.assertEquals(url,'/post/like/testblog1/')

# Code for testing api of like toggle url
	def test_apipost_like(self):
		url=reverse('like-api-toggle',args=['testblog1'])
		self.assertEquals(url,'/api/like/testblog1/')

# Code for testing post delete url
	def test_postdelete(self):
		url=reverse('post-delete',args=[1])
		self.assertEquals(url,'/post/1/delete/')

# Code for testing profile view url
	def test_Profileview(self):
		url=reverse('blog-profile',args=['testuser'])
		self.assertEquals(url,'/profileview/testuser')

# Code for testing post update url
	def test_postupdate(self):
		url=reverse('post-update',args=[1])
		self.assertEquals(url,'/post/1/update/')