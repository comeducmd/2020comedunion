from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):

    model = models.Photo


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


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"