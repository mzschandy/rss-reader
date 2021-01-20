from django.contrib import admin
from . import models

# Register your models here.
class FeedListAdmin(admin.ModelAdmin):
    list_display = ("name", "feed")

admin.site.register(models.FeedList, FeedListAdmin)