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
        return self.cat_title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ManyToManyField(Categories, related_name='category', blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    up_votes = models.ManyToManyField(User, related_name='up_votes', blank=True)
    down_votes = models.ManyToManyField(User, related_name='down_votes', blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def number_of_ups(self):
        return self.up_votes.count()

    def number_of_downs(self):
        return self.down_votes.count()

    # IS IT POSSIBLE TO DO THE BELOW????
    # class Meta:
    #     ordering = number_of_ups(self) - number_of_downs(self)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
