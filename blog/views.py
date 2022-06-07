from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from django.db.models import Count

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.annotate(counter=Count('up_votes') - Count('down_votes')).order_by('counter')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by('created_on')
        up_votes = False
        if post.up_votes.filter(id=self.request.user.id).exists():
            up_voted = True
        if post.down_votes.filter(id=self.request.user.id).exists():
            down_voted = True

        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                # "up_voted": up_voted,
                # "down_voted": down_voted
            })