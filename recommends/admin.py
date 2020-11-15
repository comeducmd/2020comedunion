from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Likes)
class RecommendAdmin(admin.ModelAdmin):
    """Custom Likes Admin"""
