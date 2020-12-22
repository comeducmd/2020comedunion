from django.db import models
from django.utils import timezone

# Create your models here.


class Photo(models.Model):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Post(models.Model):
    "Post Model Definition"

    title = models.CharField(max_length=200)
    team_name = models.CharField(max_length=100)
    team_member = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    pub_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    site_url = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_video_url(self):
        original_url = self.video_url
        if "v=" in original_url:
            return original_url.split("?v=")[1]
        else:
            return original_url.split("/")[-1]
