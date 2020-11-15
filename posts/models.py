from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    "Post Model Definition"

    title = models.CharField(max_length=200)
    team_name = models.CharField(max_length=100)
    team_member = models.ManyToManyField(
        "users.User",
        related_name="posts",
        blank=True,
    )
    pub_date = models.DateTimeField(default=timezone.now)
    pub_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
