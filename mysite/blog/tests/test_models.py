from django.test import TestCase
from blog.models import Post,TagDict
from django.urls import reverse,resolve
from django.template.defaultfilters import slugify


class ModelsTestCase(TestCase):

# Unit test for __str__ function of Post
	def test_string_representation(self):
		entry = Post(title="this new title")
		self.assertEqual(str(entry), entry.title)

# Unit test for __str__ function of TagDict
	def test_Tag(self):
		data=TagDict(tag='good')
		self.assertEqual(str(data),data.tag)

	# def test_post_has_slug(self):
     #   post = Post.objects.create(title="My first post")
      #  post.content = 'This is only for testing purpose blog',
       # post.author      = User.objects.get(email='a@c.in'),
        #post.view_count  = 0
        #post.save()
        #self.assertEqual(post.slug, slugify(post.title))