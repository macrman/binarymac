from django.contrib import admin
from myblog.models import Post, Tag

admin.site.register(Post, Tag)
