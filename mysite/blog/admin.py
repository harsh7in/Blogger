from django.contrib import admin

from .models import Post, TagDict

# Register your models here.

admin.site.register(Post)
admin.site.register(TagDict)

