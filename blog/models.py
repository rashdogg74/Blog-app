from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Categories(models.Model):
    cat_title = models.CharField(max_length=200, unique=True)
    cat_featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.cat_title}"


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ManyToManyField(Categories, related_name='category', blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitted_by")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author", default=10002)
    comment = models.TextField()
    likes = models.ManyToManyField(User, related_name='comment_like', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.comment} by {self.comment_author}"


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    up_votes = models.ManyToManyField(Post, related_name='up_votes', blank=True)


class Downvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    down_votes = models.ManyToManyField(Post, related_name='down_votes', blank=True)
