from django.db import models
from accounts.models import CustomUser


class BlogPost(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')

    def __str__(self):
        return self.title

    def is_visible_to(self, user):
        """Check if the user can view this blog post."""
        return self.visibility == 'public' or self.author == user


