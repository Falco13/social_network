from django.contrib import admin
from social_network.models import User, Post, Like, Dislike


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'created_at', 'likes', 'dislikes']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'liker', 'post', 'created_at']


@admin.register(Dislike)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'disliker', 'post', 'created_at']
