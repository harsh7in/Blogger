from django.test import TestCase
from blog.models import Post
from blog.tests.test_views import TestViews
from blog.forms import PostForm


# Code for Testing attributes of forms.py
class FormsTest(TestCase):
	def test_form(self):
		from_data={
		'title': 'my-name',
		'content': 'here i am',
		'tags': 'good'
		}
		form1=PostForm(from_data)
		self.assertTrue(form1.is_valid())