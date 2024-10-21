from django.urls import reverse

from django.contrib.auth import models as auth_models
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.
class Blogger(models.Model):
    user_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing Author object."""
        return self.user_name

    def get_absolute_url(self):
        """Returns the url to a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('user_name'),
                name='blogger_name_case_insensitive_unique',
                violation_error_message='User already exists (case insensitive match)'
            ),
        ]

class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=10000)

    def __str__(self):
        """String for representing blog post object (Title)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular blog post instance."""
        return reverse('blog-post-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']

class Comment(models.Model):
    author = models.ForeignKey(auth_models.User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing comment object (first 75 characters of description)."""
        return self.description[:75]

    def get_absolute_url(self):
        """Returns url to access a particular comment instance."""
        return reverse('comment-detail', args=[str(self.id)])

    class Meta:
        ordering = ['post_date']
