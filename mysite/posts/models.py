from django.db import models
from django.utils import timezone
from mysite import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1, related_name='authored_posts')
    # need to pass function, so default value is not static!
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def publish(self):
        self.published_at = timezone.now()
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    body = models.TextField()

    likes = models.ManyToManyField('auth.User', blank=True, related_name='comment_likes')

    created_at = models.DateTimeField(default=timezone.now)
    approved_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.approved_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.author + " on " + str(self.created_at)