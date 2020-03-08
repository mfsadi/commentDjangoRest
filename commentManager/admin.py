from django.contrib import admin
from commentManager.models import Post, Comment
from django.contrib.sites.models import Site

admin.site.register(Comment)
admin.site.register(Post)
