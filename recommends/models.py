from django.db import models

# Create your models here.
class Likes(models.Model):
    """
    How many likes did the post got?
    """
    
    liked_user = models.ManyToManyField("users.User", related_name="like")
    likes = models.IntegerField(default=0)
    liked_post = models.OneToOneField("posts.Post", on_delete=models.CASCADE)

    def count_likes(self):
        likes = self.liked_user.count()
        return likes
