from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('posts.Posts', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.author + " (" + self.created_at + ")"