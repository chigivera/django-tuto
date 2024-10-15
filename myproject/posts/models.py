from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default="fallback.png",blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __init__(self,title,content,slug=None):
    #     self.title = title
    #     self.content = content
    #     self.slug = slug
  
    
    def __str__(self):
        return self.title