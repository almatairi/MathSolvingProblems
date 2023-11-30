from django.contrib import admin
from .models import Post


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(Post, PostsAdmin)