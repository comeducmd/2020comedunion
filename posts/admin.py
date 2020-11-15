from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """Custom Post Admin """

    list_display = (
        "title",
        "team_name",
        "count_likes",
        "pub_date",
    )

    list_filter = ("team_name",)

    def count_likes(self, obj):
        return obj.likes.count_likes()