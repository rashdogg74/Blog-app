from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Upvote, Downvote
from django.db.models import Count

class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.annotate(counter=Count('up_votes') - Count('down_votes')).order_by('counter')
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by('created_on')
        up_vote = False
        
        
        # if up_vote.up_votes.filter(id=self.request.user.id).exists():
        #     up_vote = True
        
        # down_vote = False
        # if Downvote.down_votes.filter(id=self.request.user.id).exists():
        #     down_vote = True

        # return render(
        #     request, "post_detail.html",
        #     {
        #         "post": post,
        #         "comments": comments,
        #         "up_voted": up_voted,
        #         "down_voted": down_voted
        #     })