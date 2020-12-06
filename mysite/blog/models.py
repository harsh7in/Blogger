from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from .utils import get_read_time
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = RichTextUploadingField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="blog_images", height_field=None, width_field=None, max_length=None, blank=True)
    view_count  = models.IntegerField(default=0)
    favourites  = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    slug        = models.SlugField(blank=True, null=True)
    tags        = TaggableManager()
    likes       = models.ManyToManyField(User, blank=True, related_name='post_likes')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
     

    class Meta:
        ordering = ["-date_posted"]
        
    def readTIme(self):
        Read_Time=get_read_time(self.content)
        Read_Time = Read_Time[2:-3]
        return Read_Time
    
    def get_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('like-toggle', kwargs={"slug":self.slug})
    
    def get_api_like_url(self):
        return reverse('like-api-toggle', kwargs={"slug":self.slug})
