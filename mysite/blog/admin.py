from django.contrib import admin

from .models import Post, TagDict
from .models import Post,Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(TagDict)
admin.site.register(Comment)

