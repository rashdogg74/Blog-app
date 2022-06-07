from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Categories, Post, Comment, Upvote, Downvote


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    summernote_fields = ('content')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('cat_title', 'created_on')
    list_filter = ['created_on', 'cat_title']
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'post', 'created_on')
    list_filter = ['created_on']
    search_fields = ['post', 'comment_author', 'comment']


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ['user']
    search_fields = ['user']


@admin.register(Downvote)
class DownvoteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ['user']
    search_fields = ['user']
