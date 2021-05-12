from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'author')
    list_filter = ('time',)


admin.site.register(Post, PostAdmin)