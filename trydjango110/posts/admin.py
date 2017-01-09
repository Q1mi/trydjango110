from django.contrib import admin
from posts import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "update", "timestamp"]
    list_display_links = ["content",]
    list_filter = ["timestamp", "content"]
    search_fields = ["title", "content"]
    list_editable = ["title", ]

    class Meta:
        model = models.Post

# 一行代码实现model在admin中可见
admin.site.register(models.Post, PostAdmin)
