from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Count

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.annotate(counter=Count('up_votes') - Count('down_votes')).order_by('counter')
    template_name = 'index.html'
    paginate_by = 8